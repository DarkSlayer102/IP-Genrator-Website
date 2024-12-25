
// Select all list items (assumed to be IPv4 addresses)
ipv4 = document.querySelectorAll("li");

// Select the remove button (assumed to be an input element like a button)
remove_button = document.querySelector("input");

// Initialize a flag to track if the button has been clicked
let clicked = false;

// Add a click event listener to the remove button
remove_button.addEventListener("click", (event) => {
    // Loop through all the list items (IPv4 addresses)
    for (let i = 0; i < ipv4.length; i++) {
        // Set the clicked flag to true (indicating the button has been clicked)
        clicked = true;

        // Remove the current list item (IPv4 address) from the DOM
        ipv4[i].remove();

        // Redirect the browser to the "/remove" URL
        // Note: This will happen on the first iteration, so subsequent items won't be removed
        window.location.href = "/remove";
    }
});




/*


function click_remove(){
    
    for (let i=0;i<ipv4.length;i++){
        ipv4[i].addEventListener("click",(event)=>{
            ipv4[i].parentNode.removeChild(ipv4[i])
        })
    }
}


click_remove();


*/
