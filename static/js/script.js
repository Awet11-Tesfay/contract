let referenceNumber = 0; // Initial reference number, can also use a timestamp-based approach

document.getElementById('printBtn').addEventListener('click', function() {
  referenceNumber++; // Increment the reference number
  printContract(referenceNumber);
});

function printContract(referenceNumber) {
  // Display the reference number (you can replace this with your actual printing code)
  alert('Reference Number: ' + referenceNumber);

  // Add your actual printing logic here...
}
