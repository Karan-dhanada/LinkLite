
import { useEffect, useState } from "react";
import "./App.css";

const API_BASE_URL = (
  import.meta.env.VITE_API_BASE_URL ||
  "http://127.0.0.1:8000/api"
).replace(/\/+$/, "");

function App() {
  const [originalUrl, setOriginalUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [urls, setUrls] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  async function fetchUrls() {
    try {
      const response = await fetch(`${API_BASE_URL}/urls`);

      if (!response.ok) {
        throw new Error("Unable to fetch URLs");
      }

      const data = await response.json();
      setUrls(data);
    } catch (err) {
      console.error(err);
    }
  }

  useEffect(() => {
    fetchUrls();
  }, []);

  async function handleShorten(e) {
    e.preventDefault();
    setError("");
    setShortUrl("");
    setCopied(false);

    if (!originalUrl.trim()) {
      setError("Please enter a URL.");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch(`${API_BASE_URL}/shorten`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          url: originalUrl,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong");
      }

      const generatedUrl = `${API_BASE_URL}/${data.short_url}`;

      setShortUrl(generatedUrl);
      setOriginalUrl("");

      await fetchUrls();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleCopy(url) {
    try {
      await navigator.clipboard.writeText(url);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      setError("Unable to copy URL.");
    }
  }

  return (
    <div className="app">
      <nav className="navbar">
        <div className="logo">
          <span className="logo-icon">↗</span>
          LinkLite
        </div>
        <span className="nav-label">URL Shortener</span>
      </nav>

      <main className="container">
        <section className="hero">
          <span className="tag">SIMPLE. FAST. RELIABLE.</span>

          <h1>
            Shorten your links.
            <span> Share them anywhere.</span>
          </h1>

          <p>
            Transform long URLs into short, shareable links
            with LinkLite.
          </p>
        </section>

        <section className="shortener-card">
          <form onSubmit={handleShorten}>
            <label htmlFor="url">Enter your long URL</label>

            <div className="input-group">
              <input
                id="url"
                type="url"
                placeholder="https://example.com/your-long-url"
                value={originalUrl}
                onChange={(e) => setOriginalUrl(e.target.value)}
                required
              />

              <button type="submit" disabled={loading}>
                {loading ? "Creating..." : "Shorten URL"}
              </button>
            </div>
          </form>

          {error && <p className="error">{error}</p>}

          {shortUrl && (
            <div className="result">
              <div>
                <span className="result-label">
                  Your shortened URL
                </span>

                <a href={shortUrl} target="_blank" rel="noreferrer">
                  {shortUrl}
                </a>
              </div>

              <button
                className="copy-button"
                onClick={() => handleCopy(shortUrl)}
              >
                {copied ? "Copied!" : "Copy"}
              </button>
            </div>
          )}
        </section>

        <section className="history">
          <div className="history-heading">
            <h2>Your recent links</h2>
            <span>{urls.length} links</span>
          </div>

          {urls.length === 0 ? (
            <p className="empty">No shortened URLs yet.</p>
          ) : (
            urls.map((item) => {
              const link = `${API_BASE_URL}/${item.short_url}`;

              return (
                <div className="url-item" key={item.short_url}>
                  <div className="url-details">
                    <a href={link} target="_blank" rel="noreferrer">
                      {link}
                    </a>
                    <p>{item.original_url}</p>
                  </div>

                  <button
                    className="copy-button"
                    onClick={() => handleCopy(link)}
                  >
                    Copy
                  </button>
                </div>
              );
            })
          )}
        </section>
      </main>

      <footer>
        Built with React & FastAPI | LinkLite
      </footer>
    </div>
  );
}

export default App;
