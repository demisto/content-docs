import cli from 'commander';
import fs from 'fs-extra';
import {compile} from '@mdx-js/mdx';

cli.version('0.1.0')
cli.requiredOption("-f --file <mdx file to parse>")
cli.parse(process.argv)

async function parseMDX(file) {
    const contents = await fs.readFile(file, 'utf8');
    const parsed = await compile(contents)
    console.log("parsed successfully!")
}

parseMDX(cli.file)
    .then((res) => {
        process.exit(0)
    })
    .catch((reason) => {
        console.error(reason)
        process.exit(1)
})
