document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("search-btn").onclick = () => {
        const pokemon = document.getElementById("pokemon-name-input").value;

        const request = new XMLHttpRequest();

        document.querySelector(".result-container").innerHTML = null;

        request.onload = function() {

            if (this.status === 200) {
                const data = JSON.parse(this.responseText);

                const pokemon_name = data.species.name;
                const pokemon_pic = data.sprites.front_default;

                const name = document.createElement("h2");
                name.classList.add("pokemon-name");
                name.innerHTML = pokemon_name.toUpperCase();

                const picture = document.createElement("img");
                picture.src = pokemon_pic;

                // console.log(movement);
                document.querySelector(".result-container").append(picture, name);
            }

            else {
                const text = document.createElement("h2");
                text.classList.add("not-found");
                text.innerHTML = "Sorry, Pokemon Not Found";

            
                document.querySelector(".result-container").append(text);
            }  
            // console.log(pokemon_name, pokemon_pic);
        }


        request.open("GET", `https://pokeapi.co/api/v2/pokemon/${pokemon.toLowerCase()}`);
        request.send();
    }
});