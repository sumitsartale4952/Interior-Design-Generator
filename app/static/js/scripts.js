// Wait for the DOM to load before running scripts
document.addEventListener("DOMContentLoaded", function () {
  const uploadForm = document.getElementById("uploadForm");
  const roomImageInput = document.getElementById("roomImage");
  const designPromptInput = document.getElementById("designPrompt");
  const resultContainer = document.createElement("div");
  const loader = document.createElement("div");

  // Append result and loader containers// Wait for the DOM to load before running scripts
  document.addEventListener("DOMContentLoaded", function () {
    const uploadForm = document.getElementById("uploadForm");
    const roomImageInput = document.getElementById("roomImage");
    const designPromptInput = document.getElementById("designPrompt");
    const resultContainer = document.createElement("div");
    const loader = document.createElement("div");

    // Append result and loader containers
    uploadForm.appendChild(loader);
    uploadForm.appendChild(resultContainer);

    // Loader animation setup
    loader.style.display = "none";
    loader.innerHTML = `
      <div style="text-align:center; margin-top: 20px;">
          <p>Generating your design...</p>
          <img src="https://i.gifer.com/ZZ5H.gif" width="50" alt="Loading">
      </div>
  `;

    // Handle form submission
    uploadForm.addEventListener("submit", function (event) {
      event.preventDefault();

      // Validate image input
      if (!roomImageInput.files[0]) {
        alert("❗ Please upload a room image.");
        return;
      }

      // Validate design prompt input
      if (designPromptInput.value.trim() === "") {
        alert("❗ Please enter a design prompt.");
        return;
      }

      // Show loader while processing
      loader.style.display = "block";
      resultContainer.innerHTML = "";

      // Prepare form data
      const formData = new FormData();
      formData.append("roomImage", roomImageInput.files[0]);
      formData.append("designPrompt", designPromptInput.value);

      // Send data to backend
      fetch("/generate", {
        // ✅ Changed from "/upload" to "/generate"
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error(`Server Error: ${response.statusText}`);
          }
          return response.json();
        })
        .then((data) => {
          loader.style.display = "none";

          if (data.error) {
            alert(`❌ ${data.error}`);
            return;
          }

          // Display uploaded image and generated results
          resultContainer.innerHTML = `
          <h3>Your Uploaded Room:</h3>
          <img src="${data.generated_image_url}" alt="Uploaded Room" 
               style="width:60%; border-radius:10px; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">

          <h3>Generated Caption:</h3>
          <p>${data.caption}</p>

          <h3>Generated Metadata:</h3>
          <ul>
              <li><strong>Style:</strong> ${data.metadata.style}</li>
              <li><strong>Room Type:</strong> ${data.metadata.room_type}</li>
              <li><strong>Key Features:</strong> ${data.metadata.key_features.join(
                ", "
              )}</li>
              <li><strong>Color Palette:</strong> ${data.metadata.color_palette.join(
                ", "
              )}</li>
          </ul>
        `;
        })
        .catch((error) => {
          loader.style.display = "none";
          alert(
            "❌ An error occurred while generating the design. Please try again."
          );
          console.error("Error:", error);
        });
    });

    // Enhanced Mousemove Background Animation
    document.addEventListener("mousemove", function (e) {
      const uploadContainer = document.querySelector(".upload-container");
      if (uploadContainer) {
        const moveX = (e.clientX * -1) / 50;
        const moveY = (e.clientY * -1) / 50;
        uploadContainer.style.backgroundPosition = `${moveX}px ${moveY}px`;
      }
    });
  });
  uploadForm.appendChild(loader);
  uploadForm.appendChild(resultContainer);

  // Loader animation setup
  loader.style.display = "none";
  loader.innerHTML = `
      <div style="text-align:center; margin-top: 20px;">
          <p>Generating your design...</p>
          <img src="https://i.gifer.com/ZZ5H.gif" width="50" alt="Loading">
      </div>
  `;

  // Handle form submission
  uploadForm.addEventListener("submit", function (event) {
    event.preventDefault();

    // Validate image input
    if (!roomImageInput.files[0]) {
      alert("❗ Please upload a room image.");
      return;
    }

    // Validate design prompt input
    if (designPromptInput.value.trim() === "") {
      alert("❗ Please enter a design prompt.");
      return;
    }

    // Show loader while processing
    loader.style.display = "block";
    resultContainer.innerHTML = "";

    // Prepare form data
    const formData = new FormData();
    formData.append("roomImage", roomImageInput.files[0]);
    formData.append("designPrompt", designPromptInput.value);

    // Send data to backend
    fetch("/generate", {
      // ✅ Changed from "/upload" to "/generate"
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Server Error: ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => {
        loader.style.display = "none";

        if (data.error) {
          alert(`❌ ${data.error}`);
          return;
        }

        // Display uploaded image and generated results
        resultContainer.innerHTML = `
          <h3>Your Uploaded Room:</h3>
          <img src="${data.image_path}" alt="Uploaded Room" 
               style="width:60%; border-radius:10px; box-shadow: 0 2px 10px rgba(0,0,0,0.2);">

          <h3>Generated Caption:</h3>
          <p>${data.caption}</p>

          <h3>Generated Metadata:</h3>
          <ul>
              <li><strong>Style:</strong> ${data.metadata.style}</li>
              <li><strong>Room Type:</strong> ${data.metadata.room_type}</li>
              <li><strong>Key Features:</strong> ${data.metadata.key_features.join(
                ", "
              )}</li>
              <li><strong>Color Palette:</strong> ${data.metadata.color_palette.join(
                ", "
              )}</li>
          </ul>
        `;
      })
      .catch((error) => {
        loader.style.display = "none";
        alert(
          "❌ An error occurred while generating the design. Please try again."
        );
        console.error("Error:", error);
      });
  });

  // Enhanced Mousemove Background Animation
  document.addEventListener("mousemove", function (e) {
    const uploadContainer = document.querySelector(".upload-container");
    if (uploadContainer) {
      const moveX = (e.clientX * -1) / 50;
      const moveY = (e.clientY * -1) / 50;
      uploadContainer.style.backgroundPosition = `${moveX}px ${moveY}px`;
    }
  });
});
