function goToDelierForm() {
  const form = document.getElementById('my-delier-form');
  const formData = new FormData(form);
  const params = new URLSearchParams(formData).toString();
  const formUrl = "{% url 'delier_form' %}" + "?" + params;

  console.log('Form Data:', formData);
  console.log('Form URL:', formUrl);

  window.location.href = formUrl;
}
