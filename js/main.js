const search = document.getElementById("search");
const results = document.getElementById("results");
const statusEl = document.getElementById("status");

function renderExtensions(category = "all") {
    const grid = document.getElementById("extensions-grid");
    if (!grid || EXTENSIONS_DATA.length === 0) return;
    
    grid.innerHTML = "";

    const filtered = category === "all" 
        ? EXTENSIONS_DATA 
        : EXTENSIONS_DATA.filter(item => item.category === category);

    filtered.forEach(item => {
        const a = document.createElement("a");
        a.href = `https://clients2.google.com/service/update2/crx?response=redirect&prodversion=122.0&acceptformat=crx2,crx3&x=id%3D${item.id}%26installsource%3Dondemand%26uc`;
        a.className = "tile-link";
        a.innerHTML = `
            <div class="tile ${item.category}">
                <img src="${item.img}" alt="${item.title}">
                <div class="text">
                    <div class="title">${item.title}</div>
                    <div class="desc">${item.desc}</div>
                </div>
            </div>
        `;
        grid.appendChild(a);
    });

    if (filtered.length === 0) {
        grid.innerHTML = `<p style="color: #fff; grid-column: 1 / -1; text-align: center; padding: 40px;">...</p>`;
    }
}

function initExtensionFilters() {
    const buttons = document.querySelectorAll('.filter-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderExtensions(btn.dataset.category);
        });
    });
}

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

window.addEventListener('load', () => {

    renderExtensions("all");

    initExtensionFilters();

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
});
