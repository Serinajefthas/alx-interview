#!/usr/bin/node
const request = require('request');
const movie_id = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/films/${movieId}`;

request(apiUrl, function (error, response, body) {
	if (error)
		console.error('Error:', error);
	else if (response.statusCode !== 200)
        	    console.error('Status:', response.statusCode);
	else {
		const movieData = JSON.parse(body);
        	const charactersUrls = movieData.characters;

		printMovieCharacters(characters, idx);
	}
});

function (characters, idx) {
	if (idx >= characters.length)
		return;
	const characterUrl = characters[index];
	request(characterUrl, function (error, response, body) {
        	if (error) {
        		console.error('Error:', error);
		}
		else if (response.statusCode !== 200) {
        		console.error('Status:', response.statusCode);
        	}
		else {
			const characterData = JSON.parse(body);
                	console.log(characterData.name);
			printMovieCharacters(characters, idx + 1);
		}
	});
}
