#!/usr/bin/node
const req = require('request');

function getRequest(url) {
    return new Promise((resolve, reject) => {
        req.get(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else if (response.statusCode !== 200) {
                reject(new Error(`Request failed with status code ${response.statusCode}`));
            } else {
                try {
                    const movieData = JSON.parse(body);
                    const chars = movieData.characters;
                    const characterPromises = chars.map(fetchCharacter);
                    Promise.all(characterPromises)
                        .then(characterNames => {
                            resolve(characterNames);
                        })
                        .catch(reject);
                } catch (parseError) {
                    reject(parseError);
                }
            }
        });
    });
}

function fetchCharacter(characterUrl) {
    return new Promise((resolve, reject) => {
        req.get(characterUrl, (error, response, body) => {
            if (error) {
                reject(error);
            } else if (response.statusCode !== 200) {
                reject(new Error(`Request failed with status code ${response.statusCode}`));
            } else {
                try {
                    const characterData = JSON.parse(body);
                    resolve(characterData.name);
                } catch (parseError) {
                    reject(parseError);
                }
            }
        });
    });
}

const MovieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';
const CompleteUrl = `${url}/${MovieId}`;

getRequest(CompleteUrl)
    .then(characterNames => {
        characterNames.forEach(characterName => {
            console.log(characterName);
        });
    })
    .catch(error => {
        console.error(`Error: ${error}`);
    });
