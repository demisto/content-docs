const cli = require('commander');
const {readFile} = require('fs-extra');

cli.version('0.1.0')
cli.requiredOption("-f --file <mdx file to parse>")
cli.parse(process.argv)

async function parseMDX(file) {
    const mdx = await import('@mdx-js/mdx');
    const contents = await readFile(file, 'utf8');
    await mdx.default(contents)
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
