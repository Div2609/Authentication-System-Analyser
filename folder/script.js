let email_id=document.getElementById("email")
let password=document.getElementById("password")
let login=document.getElementById("login")
let signup=document.getElementById("signup")
let show = document.getElementById("show")

login.addEventListener("click",async function login(){
    const res = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email_id: email_id.value, password: password.value})
    })
    const content = await res.json()
    alert(content["message"])
})

signup.addEventListener("click",async function signup(){
    await fetch("http://127.0.0.1:5000/signup", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email_id: email_id.value, password: password.value})
    })
    alert("Added User")
})

show.addEventListener("click", async function show(){
    const res = await fetch("http://127.0.0.1:5000/")
    const content = await res.json()
    console.log(content["users"])
})
