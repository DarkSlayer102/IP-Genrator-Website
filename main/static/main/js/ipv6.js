




ipv6 = document.querySelectorAll("li");

remove_button = document.querySelector("input")


 
remove_button.addEventListener("click", (event)=>{
    for (let i=0;i< ipv6.length;i++) {
        clicked = true;
        ipv6[i].parentNode.removeChild(ipv6[i]);
        window.location.href = "/remove"
        
    }
    

})



/*

function click_remove(){
    
    for (let i=0;i<ipv6.length;i++){
        ipv6[i].addEventListener("click",(event)=>{
            ipv6[i].parentNode.removeChild(ipv6[i])
        })
    }
}


click_remove();

*/
