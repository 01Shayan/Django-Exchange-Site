// Add dynamic functionality to update rates when the origin currency changes
document.getElementById('origin-currency').addEventListener('change', (event) => {
    const selectedCurrency = event.target.value;
    alert(`Selected origin currency: ${selectedCurrency}`);
    // You can fetch new rates from the server based on the selected currency
});