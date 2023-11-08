import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: "API_KEY", // defaults to process.env["OPENAI_API_KEY"]
});

function getJSONFromResponse(response, defaultValue) {
  let text = response.choices[0]?.message?.content;
  if (text) {
    const startPrefix = "```json";
    const endPrefix = "```";

    try {
      if (text.startsWith(startPrefix) && text.endsWith(endPrefix)) {
        return text.replace(startPrefix, "").replace(endPrefix, "");
      }
    } catch (err) {
      console.log(err);
    }
  }

  return defaultValue || null;
}

const originalRes = {
  width: 2592,
  height: 1944,
};

const scaleFactor = 0.25;

const scaledRes = {
  width: Math.round(originalRes.width * scaleFactor),
  height: Math.round(originalRes.height * scaleFactor),
};

// Before the first call there was $0.23
// After a few calls it's $0.27
const user = "user";
const pass = "pass";
const basicAuth = `${user}:${pass}`;

const leftOffset = Math.round(originalRes.width / 5);
const rightOffset = Math.round(originalRes.width / 4);
const bottomOffset = Math.round(originalRes.height / 2);
const topOffset = Math.round(originalRes.height / 20);

const etop = topOffset;
const eleft = leftOffset;
const ewidth = originalRes.width - leftOffset - rightOffset;
const eheight = originalRes.height - topOffset - bottomOffset;

const width = Math.round((ewidth - eleft) * scaleFactor);
const height = Math.round((eheight - etop) * scaleFactor);

const params = {
  width,
  height,
  eleft: leftOffset,
  etop,
  ewidth: originalRes.width - leftOffset - rightOffset,
  eheight: originalRes.height - bottomOffset,
  quality: 100,
  format: "jpeg",
  timestamp: Math.round(Date.now() / 1000),
};

const queryParams = Object.entries(params)
  .map(([key, value]) => `${key}=${value}`)
  .join("&");

const imageUrl = `https://${basicAuth}@Domain/api/camera-path?${queryParams}`;

console.log({ imageUrl });

async function main() {
  const response = await openai.chat.completions.create({
    model: "gpt-4-vision-preview",
    max_tokens: 150,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            // detail: "low",
            text: `
            You're a guard and I will share you an image of the parking.

            Legend:
            B - wooden border which is on the very top of the image
            P - parking paved with cobblestones (not including grass)
            L - rectangular car lift which could go up, it's located on the center of P
            F - small fence in B on its left and on the very left of P
            G - 2-winged gate in B
            C - some car

            I will share with u an image of P.
            L is often closed (on the same level as the ground).

            Type def:
            level - false or 1-9
            
            Return only plain JSON data with a below properties:
            cars - number or false
            canPark - level - can park? false means there is absolutely no space or G is blocked, 9 means that the half of P near G is empty
            gate - bool - G is opened?
            fence - bool - F is opened?
            snow - level - how many snow on the parking, where 9 means P if fully covered by it, false means none on it
            leaves - level - how many leaves on the parking, where 9 means P if fully covered by them, false means none on it
            bw - bool - black and white image?
            lift - bool - L is opened?
            lights - bool - do you see lights on?
            night - bool - is night?
            plates - string - a list of found car plates concatenated with ","

            ### Example of response below
            {
            cars: 1,
            canPark: false,
            gate: true,
            fence: false,
            snow: 5,
            leaves: 1,
            color: true,
            lift: true,
            lights: true,
            night: true,
            plates: "LKR1111,WA23224"
            }
            ###
          `,
          },
          {
            type: "image_url",
            image_url: imageUrl,
          },
        ],
      },
    ],
  });

  const json = getJSONFromResponse(response);

  if (!json) {
    console.log(response.choices);
  } else {
    console.log(json);
  }
}
main();