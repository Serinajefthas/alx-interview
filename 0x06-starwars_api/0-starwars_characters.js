#!/usr/bin/node
const request = require('request');

function printMovieCharacters(movieId) {
    const apiUrl = `https://swapi-api.alx-tools.com/films/${movieId}`;

    request(apiUrl, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            return;
        }

        if (response.statusCode !== 200) {
            console.error('Status:', response.statusCode);
            return;
        }

        const movieData = JSON.parse(body);
        const charactersUrls = movieData.characters;

        // Fetch data for each character URL
        charactersUrls.forEach(characterUrl => {
            request(characterUrl, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error('Error:', charError);
                    return;
                }

                if (charResponse.statusCode !== 200) {
                    console.error('Status:', charResponse.statusCode);
                    return;
                }

                const characterData = JSON.parse(charBody);
                console.log(characterData.name);
            });
        });
    });
});
