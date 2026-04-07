const search = document.getElementById("search");
const results = document.getElementById("results");
const statusEl = document.getElementById("status");

function openTab(index) {
    let tabs = document.querySelectorAll('.content');
    tabs.forEach(tab => tab.classList.remove('active'));
    tabs[index].classList.add('active');
}

function loadScript(url) {
  return new Promise((resolve, reject) => {
    const s = document.createElement("script");
    s.src = url;
    s.onload = resolve;
    s.onerror = () => reject(new Error("Error during loading script"));
    document.body.appendChild(s);
  });
}

loadScript("https://github.com/Lutsic/crx-extension-downloader/releases/download/release/data.js")
  .then(() => {
    statusEl.textContent = "All data loaded correctly";
  })
  .catch(err => {
    console.error(err);
    statusEl.textContent = "Error during data loading: " + err.message;
  });

search.oninput = () => {
  const q = search.value.toLowerCase();
  results.innerHTML = "";

  if (typeof DATA === "undefined" || !q) return;

  let count = 0;

  for (const name in DATA) {
    if (name.toLowerCase().includes(q)) {
      const li = document.createElement("li");
      const a = document.createElement("a");

      a.textContent = name;
      a.href = DATA[name];
      a.target = "_blank";

      li.appendChild(a);
      results.appendChild(li);

      if (++count >= 100) break;
    }
  }
};
