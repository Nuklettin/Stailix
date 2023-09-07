import "dotenv/config";
import { Midjourney } from "../src";

let prompt = "https://i.imgur.com/Z5cfxx9.png, angry bald man with a bushy moustache, logo, simplistic, minimalistic";

/**
 *
 * a simple example of using the imagine api with ws
 * ```
 * npx tsx example/imagine-ws.ts
 * ```
 */
async function main() {
  const client = new Midjourney({
    ServerId: "1102396513679843438",
    ChannelId: "1102397995569397831",
    SalaiToken: "MTEwMjIwMzI3MzY4MDgwMTg2Mw.Gmo4CQ.lLDtWnCSOY0ewiaTPpVlYcN4Eu6TdDu2n6BbkE",
    HuggingFaceToken: <string>process.env.HUGGINGFACE_TOKEN,
    Debug: true,
    Ws: true,
  });
  await client.Connect();
  const Imagine = await client.Imagine(
    prompt,
    (uri: string, progress: string) => {
      console.log("Imagine.loading", uri, "progress", progress);
    }
  );
  console.log({ Imagine });
  if (!Imagine) {
    return;
  }
  /*const reroll = await client.Reroll({
    msgId: <string>Imagine.id,
    hash: <string>Imagine.hash,
    flags: Imagine.flags,
    loading: (uri: string, progress: string) => {
      console.log("Reroll.loading", uri, "progress", progress);
    },
  });
  console.log({ reroll });

  const Variation = await client.Variation({
    index: 2,
    msgId: <string>Imagine.id,
    hash: <string>Imagine.hash,
    flags: Imagine.flags,
    loading: (uri: string, progress: string) => {
      console.log("Variation.loading", uri, "progress", progress);
    },
  });

  console.log({ Variation });
  if (!Variation) {
    return;
  }
  const Upscale = await client.Upscale({
    index: 2,
    msgId: <string>Variation.id,
    hash: <string>Variation.hash,
    flags: Variation.flags,
    loading: (uri: string, progress: string) => {
      console.log("Upscale.loading", uri, "progress", progress);
    },
  });
  console.log({ Upscale });*/

  client.Close();
}
main()
  .then(() => {
    console.log("finished");
    process.exit(0);
  })
  .catch((err) => {
    console.log("finished");
    console.error(err);
    process.exit(1);
  });
