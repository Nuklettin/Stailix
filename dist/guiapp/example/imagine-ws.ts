import "dotenv/config";
import { Midjourney } from "../src";

let prompt = "https://i.imgur.com/Ppcg7ZX.png, (fascinating   Man (Regular Fit) Business black leather jacket),(  Man (Expensive) fashion ), ((Regular Fit) Man), Business Man style design, ,((Black Background)) inspired fashion design, full body shot, ultra detailed , dream-like quality, studio lighting, professional fashion photography , hyper realistic,UHD,32K --ar 133:200";

/**
 *
 * a simple example of using the imagine api with ws
 * ```
 * npx tsx example/imagine-ws.ts
 * ```
 */
async function main() {
  const client = new Midjourney({
    ServerId: "1153285309530918922",
    ChannelId: "1153285309530918925",
    SalaiToken: "MjA1NzMyNjYyNzIyMjk3ODU2.YTtI2A.IXFdMNhH5VDwKx3371q_9DyGDOU",
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
