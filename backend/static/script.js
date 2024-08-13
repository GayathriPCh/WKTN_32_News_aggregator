function analyzeArticle(articleId) {
    fetch(`/analyze?id=${articleId}`)
        .then(response => response.json())
        .then(data => {
            if (data.analysis) {
                document.getElementById(`analysis-${articleId}`).innerText = data.analysis;
            } else {
                document.getElementById(`analysis-${articleId}`).innerText = 'Analysis not available.';
            }
        })
        .catch(error => {
            console.error('Error fetching analysis:', error);
            document.getElementById(`analysis-${articleId}`).innerText = 'Error fetching analysis.';
        });
}
