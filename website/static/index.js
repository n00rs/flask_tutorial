function deleteNote(noteId) {
  fetch("/delete_note", {
    body: JSON.stringify({ noteId }),
    method: "POST",
  }).then(() => window.location.href("/"));
}
