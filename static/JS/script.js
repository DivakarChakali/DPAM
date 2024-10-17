let happyCustomersVal = 0;
let movesCompletedVal = 0;
let yearsOfExpVal = 0;
let happycustomersCount = setInterval(()=> {
  let count = document.getElementById("happyCustomers");
  count.innerHTML =++happyCustomersVal;
  if (happyCustomersVal === 856) {
    clearInterval(happycustomersCount);
  }
}, )
let movesCompletedCount = setInterval(()=> {
  let count = document.getElementById("movesCompleted");
  count.innerHTML =++movesCompletedVal;
  if (movesCompletedVal === 1023) {
    clearInterval(movesCompletedCount);
  }
}, )
let yearsOfExpCount = setInterval(()=> {
  let count = document.getElementById("yearsOfExp");
  count.innerHTML = ++yearsOfExpVal;
  if (yearsOfExpVal === 6) {
    count.innerHTML = `${yearsOfExpVal}+`;
    clearInterval(yearsOfExpCount);
  }
}, 1000)
