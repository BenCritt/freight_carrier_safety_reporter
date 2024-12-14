# This is the code for the Freight Carrier Safety Reporter
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def freight_safety(request):
    form = CarrierSearchForm(request.POST or None)
    carrier = None
    error = None
    # safety_score = None ~ I'm still working on this feature.

    if request.method == "POST" and form.is_valid():
        search_value = form.cleaned_data["search_value"]

        try:

            # Ensure the search is conducted only with a DOT number
            carrier = get_fmcsa_carrier_data_by_usdot(search_value)

            if not carrier:
                error = "Carrier not found in FMCSA.  Please verify you're submitting a valid DOT Number."

            """
            I'm still working on this feature.
            
            if carrier:
                safety_score = calculate_safety_score(carrier)  # Calculate the safety score
                
                # Check if the user clicked the 'Download PDF' button
                if 'download_pdf' in request.POST:
                    return generate_pdf(carrier, safety_score)  # Trigger the PDF generation
            else:
                error = "Carrier not found in FMCSA."
            """
        except requests.exceptions.RequestException as e:
            # Catch any errors related to the API request
            error = f"There was an issue retrieving the carrier data. Please try again later. Error: {str(e)}"

    return render(
        request,
        "projects/freight_safety.html",
        {
            "form": form,
            "carrier": carrier,
            "error": error,
        },  # "safety_score": safety_score
    )
