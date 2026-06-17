document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("search-input");
    const resultsDiv = document.getElementById("search-results");

    if (!input || !resultsDiv) return;

    let debounceTimer;

    input.addEventListener("input", () => {
        clearTimeout(debounceTimer);
        const query = input.value.trim();

        if (!query) {
            resultsDiv.innerHTML = "";
            return;
        }

        debounceTimer = setTimeout(async () => {
            try {
                const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
                const data = await response.json();
                renderResults(data.results);
            } catch (err) {
                resultsDiv.innerHTML = `<p style="color:#fc8181">Search error: ${err.message}</p>`;
            }
        }, 300);
    });

    function renderResults(results) {
        if (!results || results.length === 0) {
            resultsDiv.innerHTML = `<p style="color:#718096;font-size:0.85rem">No servers found.</p>`;
            return;
        }

        resultsDiv.innerHTML = results.map(server => `
            <div class="search-result-item">
                <a href="/server/${encodeURIComponent(server.Hostname)}">${server.Hostname}</a>
                <span class="badge ${server.Status && server.Status.toLowerCase() === 'online' ? 'badge-online' : 'badge-offline'}">
                    ${server.Status || 'Unknown'}
                </span>
            </div>
        `).join("");
    }
});
