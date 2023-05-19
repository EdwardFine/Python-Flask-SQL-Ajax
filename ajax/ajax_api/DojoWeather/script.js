var hotTemps = document.querySelectorAll(".hot");
var coldTemps = document.querySelectorAll(".cold");
var unit_value = "";
var unit_selector = document.querySelector("#unit");
var days = document.querySelectorAll(".day-text");

async function getWeather(){
    var res = await fetch('http://api.openweathermap.org/data/2.5/forecast?id=5392171&appid={{REDACTED}}');
    var weather = await res.json();
    console.log(weather);
    var temps = [[],[]];
    for(var i=2;i<days.length;i++){
        days[i].innerHTML = weather.list[8*i].dt_txt.slice(5,10);
    }
    return weather;
}

getWeather();

async function setUnit(element){
    if(element.value != unit_value){
        var res = await fetch('http://api.openweathermap.org/data/2.5/forecast?id=5392171&appid={{REDACTED}}');
        var weather = await res.json();
        if(element.value == "°C"){
            for(var i=0;i<hotTemps.length;i++){
                    hotTemps[i].innerText = Math.round(weather.list[i*8+2].main.temp_max-273.15);
                    coldTemps[i].innerText = Math.round(weather.list[i*8+4].main.temp_min-273.15);
                }
        }else{
            for(var i=0;i<hotTemps.length;i++){
                hotTemps[i].innerText = Math.round((weather.list[i*8+2].main.temp_max-273.15)*9/5+32);
                coldTemps[i].innerText = Math.round((weather.list[i*8+4].main.temp_min-273.15)*9/5+32);
            }
        }
    unit_value = element.value;
    }
}

setUnit(unit_selector);

function acceptCookie(element){
    element.parentElement.remove();
}



