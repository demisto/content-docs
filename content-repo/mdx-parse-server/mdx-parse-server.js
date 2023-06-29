import {compile} from '@mdx-js/mdx';
import readFile from 'fs-extra';
import http from 'http';

function requestHandler(req, res) {
    // console.log(req)
    if (req.method !== 'POST') {
        res.statusCode = 405
        res.end('Only POST requests are supported.')
        return
    }
    let body = ''
    req.setEncoding('utf8');
    req.on('data', function (data) {
        body += data
    })
    req.on('end', async function () {
        // console.log('Body length: ' + body.length)
        try {
            const contents = await readFile(file)
            await compile(contents)
            res.end('Markdown data parsed successfully.')
        } catch (error) {
            res.statusCode = 500
            res.end("Error while parsing Markdown data: " + error)   
        }
    })
}

const server = http.createServer(requestHandler);

server.listen(6060, (err) => {
    if (err) {
        return console.log('something bad happened', err)
    }
    console.log(`MDS server is listening on port: 6060`)
});
