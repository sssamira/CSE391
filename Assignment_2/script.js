function calculate(){
    var inp = document.cal.numbers.value;
    var x = inp.split(",").map(function(item)
    {
        return parseFloat(item.trim());
    });
    if (x.length!=0){
        var max = maxi(x);
        var min = mini(x);
        var su = sum(x);
        var av = avg(x);
        var re = rev(x);
    }
    document.getElementById("max").textContent = "Max: " + max;
    document.getElementById("min").textContent = "Min: " + min;
    document.getElementById("sum").textContent = "Sum: " + su;
    document.getElementById("avg").textContent = "Avarage: " + av;
    document.getElementById("rev").textContent = "Reverse Order: " + re ;
}

function maxi(a){
    return Math.max(...a);
}
function mini(a){
    return Math.min(...a);
}
function sum(a){
    return a.reduce((acc, num) => acc + num, 0);
}
function avg(a){
    let s = sum(a);
    return s/a.length
}
function rev(a){
    return a.slice().reverse();
}

function convert(){
    const w = parseFloat(document.getElementById("val").value);
    const choice = document.getElementById("choice").value;

    if (choice === "ktl"){
        var res = w*0.4536;
        document.getElementById("result").textContent = `${res.toFixed(4)} pounds`;
    } 
    else if (choice === "ltk"){
        var res = w*2.2046;
        document.getElementById("result").textContent =`${res.toFixed(4)} kilograms`;
    }
}

function qt(){
    const q = [
        "The less we deserve good fortune, the more we hope for it.",
        "Fortune and love favor the brave.",
        "Formal education will make you a living; self-education will make you a fortune.",
        "Live as brave men; and if fortune is adverse, front its blows with brave hearts.",
        "Fortune favors the prepared mind.",
        "Fortune befriends the bold.",
        "Come what may, all bad fortune is to be conquered by endurance.",
        "There are good and bad times, but our mood changes more often than our fortune.",
        "Fortune favors the audacious.",
        "From my tribe I take nothing, I am the maker of my own fortune.",
        "Diligence is the mother of good fortune.",
        "Friends and acquaintances are the surest passport to fortune."
        ]

    document.getElementById("qu").textContent = q[Math.floor(Math.random() * q.length)];
    
}
window.onload = qt;


function color(x){
    const clr_button = document.querySelector(".quote-box");
    clr_button.style.borderColor = color;
}