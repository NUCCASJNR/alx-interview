#!/usr/bin/node

const request = require('request');
const SwapFilmUrl = 'https://swapi-api.alx-tools.com/api/films/'


// Fetch Films
function fetchFims(MovieId) {
    const MovieUrl = SwapFilmUrl + MovieId
    return new Promise((resolve, reject) => {
        request(MovieUrl, (error, response, body) => {
            if (error) {
                reject(error);
                return;
            }
            if (response.statusCode !== 200) {
                reject(new Error('Failed to Fetch Movie'));
                return;
            }
            try {
                const MovieData = JSON.parse(body);
                resolve(MovieData);
            } catch (ParseError) {
                reject(parseError);
            }
        });
    });
}
const MovieIdArg = process.argv[2]
if (!MovieIdArg) {
    console.error('Please provide Movie Id');
    process.exit(1)
}

fetchFims(MovieIdArg)
    .then(MovieData => {
    console.log('Star Wars Movie Information: ');
    console.log(`Title: ${MovieData.title}`);
    console.log(`Director: ${MovieData.director}`);
    console.log(`release_date: ${MovieData.release_date}`)
})
    .catch(error => {
        console.error(`Error: ${error}`)
    });