async function downloadBlob(e) {
    e.preventDefault();

    try {
        const originalUrl = new URL(e.currentTarget.dataset.source || e.currentTarget.href);
        const response = await fetch(originalUrl.toString());
        if (!response.ok) {
            throw new Error("Fetch failed");
        }
        const blob = await response.blob();
        const fileUrl = window.URL.createObjectURL(blob);

        const segments = originalUrl.pathname.split('/');
        const fileName = decodeURIComponent(segments.pop() || segments.pop());

        const anchorElement = document.createElement('a');

        anchorElement.href = fileUrl;
        anchorElement.download = fileName;
        anchorElement.style.display = 'none';

        document.body.appendChild(anchorElement);

        anchorElement.click();
        anchorElement.remove();

        window.URL.revokeObjectURL(fileUrl);
    } catch (error) {
        console.error("There has been a problem downloading the blob:", error);
    }
}
