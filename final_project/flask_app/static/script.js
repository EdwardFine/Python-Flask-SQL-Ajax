var container = document.querySelector(".container")
var banner = document.querySelector("#banner")
var title = document.querySelector("title")
var id = document.querySelector("#id")
console.log(id);

async function getHomeGames(){
    var res = await fetch("http://localhost:5000/home_games");
    var games = await res.json();
    for(var i=0;i<20;i++){
        console.log(games.results[i])
        container.innerHTML += `<form action='/check_game' method='post'><input type='hidden' name='id' value='${games.results[i].id}'> <input type='hidden' name='title' value='${games.results[i].name}'><button class='game-card'><img src='${games.results[i].background_image}' class='game-image' alt='${games.results[i].slug}'><h1>${games.results[i].name}</h1></button></form>`;
    }
    return games;
}

async function viewOneGame(id){
    var res = await fetch(`http://localhost:5000/single_game/${id}`);
    var game = await res.json();
    title.innerText=`Viewing ${game.name}`
    banner.innerHTML=`<div class="game-header-image" style="background-image: url(${game.background_image});">
    </div>
    <div class="game-header-text">
        <span style="background-color:rgb(133, 111, 255); padding:.125em .25em .125em .25em">${game.name}</span> 
    </div>`
    console.log(game)
}

async function search(){
    let params = new URL(document.location).searchParams;
    let title = document.querySelector(".search-title");
    title.innerHTML += params.get('query');
    var form = new FormData();
    form.append('query',params.get("query"))
    var res = await fetch("http://localhost:5000/search",{method:'POST',body:form});
    var games = await res.json();
    for(var i=0;i<20;i++){
        console.log(games.results[i])
        container.innerHTML += `<form action='/check_game' method='post'><input type='hidden' name='id' value='${games.results[i].id}'> <input type='hidden' name='title' value='${games.results[i].name}'><button class='game-card'><img src='${games.results[i].background_image}' class='game-image' alt='${games.results[i].slug}'><h1>${games.results[i].name}</h1></button></form>`;
    }
    return games;
}

if(title.innerText=="FanRequest Home"){
    getHomeGames();
}else if(title.innerText=="View Game"){
    viewOneGame(id.value)
}