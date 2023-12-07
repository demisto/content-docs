import { compile } from '@mdx-js/mdx';
import http from 'http';

function requestHandler(req, res) {
    // console.log(req)
    if (req.method != 'POST') {
        res.statusCode = 405
        res.end('Only POST is supported')
        return
    }
    let body = ''
    req.setEncoding('utf8');
    req.on('data', function (data) {
        body += data
    })
    req.on('end', async function () {
        //   console.log('Body length: ' + body.length)
        try {
            const parsed = await compile(body)
            res.end('Successfully parsed mdx')
        } catch (error) {
            res.statusCode = 500
            res.end("MDX parse failure: " + error)   
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

