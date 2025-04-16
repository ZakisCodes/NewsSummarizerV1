// redirect to result.html


async function SendNews(event){
  // preventing the page from reloading
  event.preventDefault();  
    // store the articles user give
  const newsText = document.getElementById("InputText").value;
  sessionStorage.setItem("newsText1", newsText);
  // sessionStorage.setItem("newsText", newsText);
  const loader = document.querySelector(".loader-container");
  loader.style.display = "flex";
  
  const form_container = document.querySelector(".form-container");
  form_container.style.display = 'none';

  const response = await fetch("/api/summarizer", {
    method:"POST",
    headers:{
      "Content-Type": "Application/json"
    },
    body:  JSON.stringify({"news": newsText})
  });
  
  if (response.ok){
    const data  = await response.json();
    sessionStorage.setItem("response", JSON.stringify(data));
    // redirect to result page
    window.location.href = "/result";
  }else{
    alert("Error found in API call")
  };

 
}





