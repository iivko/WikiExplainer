import { useState } from "react"
import { Search, Loader2 } from "lucide-react"

function App() {
  const [topic, setTopic] = useState("")
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState("")

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!topic.trim()) return

    setLoading(true)
    setError("")
    setResult(null)

    try {
      const response = await fetch("http://127.0.0.1:8000/api/exp/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ topic: topic.trim() }),
      })

      if (!response.ok) throw new Error("Failed to get explanation")

      const data = await response.json()
      console.log(data)
      setResult(data)
    } catch (err) {
      console.error(err)
      setError("Something went wrong. Please try again.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8 px-4">
      <div className="max-w-4xl mx-auto">

        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">Topic Explainer</h1>
          <p className="text-lg text-gray-600">Enter any topic and get an instant explanation with visuals</p>
        </div>

        {/* Form */}
        <div className="max-w-xl mx-auto mb-8">
          <form onSubmit={handleSubmit} className="relative">
            <div className="relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 h-5 w-5" />
              <input
                type="text"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
                placeholder="Enter a topic (e.g., Black Holes, Quantum Physics...)"
                className="w-full pl-12 pr-4 py-4 text-lg border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all duration-200 shadow-sm"
                disabled={loading}
              />
            </div>
            <button
              type="submit"
              disabled={loading || !topic.trim()}
              className="w-full mt-4 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-4 px-6 rounded-xl transition-colors duration-200 shadow-md disabled:cursor-not-allowed cursor-pointer"
            >
              {loading ? (
                <div className="flex items-center justify-center">
                  <Loader2 className="animate-spin h-5 w-5 mr-2" />
                  Getting explanation...
                </div>
              ) : (
                "Explain This Topic"
              )}
            </button>
          </form>
        </div>

        {/* Error */}
        {error && (
          <div className="max-w-xl mx-auto mb-8">
            <div className="bg-red-50 border border-red-200 rounded-xl p-4">
              <p className="text-red-700 text-center">{error}</p>
            </div>
          </div>
        )}

        {/* Result */}
        {result && (
          <div className="max-w-3xl mx-auto">
            <div className="bg-white rounded-xl shadow-lg overflow-hidden">
              <div className="bg-gradient-to-r from-blue-600 to-indigo-600 px-6 py-8">
                <h2 className="text-3xl font-bold text-white text-center">{result.topic}</h2>
              </div>

              <div className="p-6 space-y-6">
                <div className="relative w-full h-64 md:h-80 rounded-xl overflow-hidden bg-gray-100">
                  <img
                    src={result.image_url || "/placeholder.svg"}
                    alt={result.topic}
                    className="w-full h-full object-cover"
                    crossOrigin="anonymous"
                  />
                </div>

                <div className="space-y-4">
                  <p className="text-gray-700 leading-relaxed text-lg">
                    {result.text.text}
                  </p>

                  <div>
                    <h3 className="text-xl font-semibold text-gray-800 mt-6 mb-2">Interesting Facts:</h3>
                    <ul className="list-disc list-inside space-y-2 text-gray-600">
                      {result.text.facts.map((fact, idx) => (
                        <li key={idx}>{fact}</li>
                      ))}
                    </ul>
                  </div>
                </div>

                <div className="flex flex-col sm:flex-row gap-3 pt-4 border-t border-gray-200">
                  <button
                    onClick={() => {
                      setResult(null)
                      setTopic("")
                    }}
                    className="flex-1 bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium py-3 px-6 rounded-lg transition-colors duration-200 cursor-pointer"
                  >
                    Search Another Topic
                  </button>
                  <button
                    onClick={() =>
                      navigator.clipboard.writeText(
                        `${result.topic}\n\n${result.text.text}\n\nFacts:\n- ${result.text.facts.join("\n- ")}`
                      )
                    }
                    className="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-6 rounded-lg transition-colors duration-200 cursor-pointer"
                  >
                    Copy Explanation
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Footer */}
        <div className="text-center mt-12 text-gray-500">
          <p>Powered by AI • Get instant explanations for any topic</p>
        </div>
      </div>
    </div>
  )
}

export default App
