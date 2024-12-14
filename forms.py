# Freight Carrier Safety Reporter
class CarrierSearchForm(forms.Form):
    search_value = forms.CharField(label="Enter USDOT Number", max_length=50)

    # Handle an invalid submission.
    def clean_search_value(self):
        data = self.cleaned_data["search_value"]

        # Ensure the USDOT number is numeric
        if not data.isdigit():
            raise forms.ValidationError("Please enter a valid USDOT number.")

        return data
