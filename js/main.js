const globalContainer = document.getElementById("global-search-container");
const results = document.getElementById("results");
const statusEl = document.getElementById("status");
const searchInput = document.getElementById("search");
const globalToggle = document.getElementById("global-toggle");
const grid = document.getElementById("extensions-grid");
const filtersPanel = document.getElementById("filters-panel");


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

// Global search checkbox
    globalToggle.addEventListener('change', () => {
        isGlobalSearch = globalToggle.checked;

        if (isGlobalSearch) {
            grid.style.display = "none";
//            globalContainer.style.display = "block";
            results.style.display = "block";
        } else {
            grid.style.display = "grid";
 //           globalContainer.style.display = "none";
             results.style.display = "none";
             renderExtensions("all"); 
        }
    });

    // search
   globalContainer.oninput = () => {
        const q = globalContainer.value.toLowerCase();
        results.innerHTML = "";
        if (typeof DATA === "undefined" || !q) return;

        if (isGlobalSearch){
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
                if (++count >= 50) break;
       
    }   else {
    
        }
        }
        }
    };


    loadScript("https://github.com/Lutsic/crx-extension-downloader/releases/download/release/data.js")
        .then(() => {
            statusEl.textContent = "✓";
        })
        .catch(err => {
            console.error(err);
            statusEl.textContent = "Error during data loading: " + err.message;
        });

});
