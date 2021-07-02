const africanCountries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina-Faso', 'Burundi', 'Cabo-Verde', 'Cameroon', 'Central-African-Republic', 'Chad', 'Comoros', 'Congo-Democratic-Republic-of', 'Congo', "Cote-d-Ivoire", 'Djibouti', 'Egypt', 'Equatorial-Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao-Tome-and-Principe', 'Senegal', 'Seychelles', 'Sierra-Leone', 'Somalia', 'South-Africa', 'South-Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

let baseUrl = 'https://www.countries-ofthe-world.com/flags-normal/flag-of-'


function renderCard(africanCountries){
    for (let i=0; i<africanCountries.length; i++){
        let li = document.createElement('li');
        let countryTitle = document.createElement('h3');
        let img = document.createElement('img')
        img.src = `${baseUrl}${africanCountries[i]}.png`
        countryTitle.textContent = africanCountries[i]
        li.append(img, countryTitle)
        document.querySelector('#country_list').append(li)
    }
    document.querySelector('div ul li').remove()
  }

  renderCard(africanCountries);

