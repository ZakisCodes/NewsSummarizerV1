/*
const response = await fetch("/api/summarizer", {
  method:"POST",
  headers:{
    "Content-Type": "Application/json"
  },
  body:  JSON.stringify({"news": article})
});
*/
window.addEventListener("DOMContentLoaded", async ()=>{
  const response = sessionStorage.getItem("response");
  const Text = sessionStorage.getItem("newsText1");
  if (response){
    console.log(Text);
    const data = await JSON.parse(response);
    document.querySelector(".headline").innerText = data.Headline;
    document.querySelector(".topic-tag").innerText = data.Topic;
    document.querySelector(".summary").innerText = data.Summary;
    document.querySelector(".rating-value").innerText = data.Readability;
    document.querySelector(".stars").innerText = data.Star;
  } else {
    document.querySelector(".summary").innerText = "Error found";
  };
});
