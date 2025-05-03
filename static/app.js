document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  const submitBtn = document.querySelector("button[type=submit]");
  const splitField = document.querySelector("input[name=split_mask]");
  // Disable submit on click and show loading
  form.addEventListener("submit", () => {
    submitBtn.disabled = true;
    submitBtn.textContent = "Calculating...";
  });
  // Copy TF to clipboard
  document.querySelector("#copy-tf")?.addEventListener("click", () => {
    const tfArea = document.querySelector("#tf-template");
    tfArea.select();
    document.execCommand("copy");
    alert("Terraform template copied!");
  });
});