var json_user = document.querySelector("#json_user");
var get_user = document.querySelector("#user-input")

async function getUser(){
    var user = await fetch(`https://api.github.com/users/${get_user.value}`);
    var user_object = await user.json();
    console.log(user_object)
    json_user.innerHTML=`<h1>${user_object.login} has ${user_object.followers} followers.`
    json_user.innerHTML+=`<img src='${user_object.avatar_url}'>`
    return user_object; 
}