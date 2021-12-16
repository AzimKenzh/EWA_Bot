export function formatDate(date_str) {
  const formatted_date = new Date(date_str);
  let options = {
    year: "numeric",
    month: "long",
    day: "numeric",
  };
  return formatted_date.toLocaleDateString(
    "en-EN",
    options
  );
}
