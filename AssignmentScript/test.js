const { exec } = require("child_process");

const fs = require("fs");
const path = require("path");
const htmlFileStart = `
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
        * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        background-color: #fff !important;
        word-wrap: break-all;
        overflow: hidden;
      }
      pre {
        white-space: pre-wrap;
      }
    
    .container {
        width: 100%;
        height: 100%;
        /* background-color: #f2f2f2; */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .container > * {
        width: 100%;
        margin: 0 10px;
        padding: 10px 50px;
    }
    
    .content {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: left;
    }
    
    .content > * {
        width: 100%;
        margin: 0 10px;
        padding: 10px 0;
    }
    
    .solution {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        justify-content: center;
        text-align: left;
    }
    
    .solution > * {
        width: 50%;
        margin: 15px 10px;
        padding: 10px 50px;
    }
    </style>

    <link href="https://unpkg.com/prismjs@1.29.0/themes/prism.min.css" rel="stylesheet" />
    <script src="https://unpkg.com/prismjs@1.29.0/components/prism-core.min.js"></script>
	<script src="https://unpkg.com/prismjs@1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <h1>Assignment 3</h1>
`;

const htmlFileEnd = `
            </div>
        </div>
    </body>
</html>
`;

async function main() {
  const dirName = "Assignment3";
  const dirPath = path.join(__dirname, "../", dirName);
  console.log(dirPath);
  const files = fs.readdirSync(dirPath);

  let questionsHtmls = ``;

  for (let file of files) {
    console.log(file);
    const filePath = path.join(__dirname, "../Assignment3/", file);

    const questionHtml = `
    <div class="question">
        1. Create a python script
    </div>
    `;

    const sourceCode = fs.readFileSync(filePath, {
      encoding: "utf-8",
      flag: "r",
    });

    const codeHtml = `
    <pre><code class="language-python">${sourceCode}</code></pre>
    `;

    const childProcess = exec(`python3 ${filePath}`, {
      shell: true,
    });

    let programOutput = "";
    childProcess.stdout.on("data", (chunk) => {
      process.stdout.write(chunk);
      programOutput += chunk;
    });

    process.stdin.pipe(childProcess.stdin);

    await new Promise((resolve) => {
      childProcess.on("close", resolve);
    });

    const outputHtml = `
    <pre><code class="language-shell">${programOutput}</code></pre>
    `;

    const solutionHtml = `
    <div class="solution">
    ${codeHtml}
    ${outputHtml}
    </div>
    `;

    const singleQuestionBlockHtml = `
        <div class="content">
        ${questionHtml}
        ${solutionHtml}
        </div>
    `;

    questionsHtmls += singleQuestionBlockHtml;
  }

  const fullHtml = `
  ${htmlFileStart}
  ${questionsHtmls}
  ${htmlFileEnd}
  `;
  const htmlFilePath = path.join(__dirname, `./${dirName}.html`);
  fs.writeFileSync(htmlFilePath, fullHtml);

  console.log(`file:///${htmlFilePath}`);
}

main();
