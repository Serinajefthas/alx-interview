#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    fetchCharacters(characters, 0);
  }
});

function fetchCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  const characterUrl = characters[index];

  request(characterUrl, function (error, response, body) {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Unexpectedstatus code:', response.statusCode);
    } else {
      const character = JSON.parse(body);
      console.log(character.name);

      fetchCharacters(characters, index + 1);
    }
  });
}
