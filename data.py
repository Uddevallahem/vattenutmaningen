import pandas as pd
import streamlit as st


def format_number(number):
    return f"{number:,}".replace(",", " ")


# Läs in Excel-filen
file_path = "Data.xlsx"
df = pd.read_excel(file_path)


# Sortera efter minskning för månad och år (lägre procent är bättre, alltså mer negativt)
df_sorted_month = df.sort_values(by='Minskning_månad').head(3)
df_sorted_year = df.sort_values(by='Minskning_år').head(3)

# Visualisering av leaderboard med medaljer
medal_icons = ["🥇", "🥈", "🥉"]

st.title("Vattenutmaningen 🏆")
st.write("_(Exempelvis - Kan vi spara 10% tillsammans?)_")

# Månadens leaderboard
st.subheader("Top 3 hyresgäster som sparat mest vatten den här månaden:")
for i, row in enumerate(df_sorted_month.itertuples(), start=0):
    # Visa procentvärden som heltal, multiplicerat med 100 och utan minustecken
    minskning_månad = f"{abs(int(row.Minskning_månad * 100))}%"  # Tar bort minustecknet, multiplicerar med 100 och rundar till heltal
    st.write(f"{medal_icons[i]} **{row.Objekt}** - {minskning_månad} minskning")

# Årets leaderboard
st.subheader("Top 3 hyresgäster som sparat mest vatten under året (2025):")
for i, row in enumerate(df_sorted_year.itertuples(), start=0):
    # Visa procentvärden som heltal, multiplicerat med 100 och utan minustecken
    minskning_år = f"{abs(int(row.Minskning_år * 100))}%"  # Tar bort minustecknet, multiplicerar med 100 och rundar till heltal
    st.write(f"{medal_icons[i]} **{row.Objekt}** - {minskning_år} minskning")

st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
st.subheader("Totala besparning för samtliga hyresgäster under 2025:")
# Hämta värdet för 'Minskning_2025' från den första raden
minskning_2025 = df.loc[0, 'Minskning_2025']  # Första raden, kolumnen 'Minskning_2025'
# Maxvärde för progress bar
max_value = 438158000
# Visa progress bar från 0 till maxvärdet
st.progress(minskning_2025 / max_value)  # Progress bar baserat på det faktiska värdet

minskning_2025 = round(minskning_2025)
minskning_2025 = format_number(minskning_2025)
st.write(f"Ni har tillsammas sparat {minskning_2025} liter vatten, fantastiskt jobbat! 🎉")
st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

# Åtgärdsförslag
def show_actions():
    st.subheader("Förslag på åtgärder för att minska vattenförbrukningen:")

    # Förslag 1
    with st.expander("💧 Stäng av vattnet när du tvålar in dig eller schamponerar håret"):
    #    st.image("https://example.com/duschmunstycke.jpg", width=150)  # Ersätt med riktig bild-URL
        st.write("En medveten dusch kan göra stor skillnad i vattenförbrukningen.")
        
        showers_per_week = st.slider(
            "Hur många duschar tar du per vecka?", 
            min_value=1, 
            max_value=14, 
            value=7, 
            step=1,
            key="showers_slider"
        )
        
        liters_saved = showers_per_week * 9  # Exempel: 9 liter per dusch
        st.write(f"Du sparar ungefär **{liters_saved} liter vatten per vecka** genom att använda ett vattensparande duschmunstycke.")
        
        if st.button("Jag har installerat detta!"):
            st.success("Bra jobbat! Du är ett steg närmare att spara vatten!")

    # Förslag 2
    with st.expander("🚿 Duscha kortare"):
     #   st.image("https://example.com/dusch.jpg", width=150)  # Ersätt med riktig bild-URL
        st.write("Försök att minska duschtiden.")
        
        temp_shower_slider = st.slider(
            "Hur många duschar tar du per vecka?", 
            min_value=1, 
            max_value=14, 
            value=7, 
            step=1,
            key="temp_shower_slider"
        )
        
        temp_liters_saved = temp_shower_slider * 8  # Exempel: 8 liter per dusch
        st.write(f"Du sparar ungefär **{temp_liters_saved} liter vatten per vecka** genom att sänka vattentemperaturen.")

        if st.button("Jag har sänkt temperaturen!"):
            st.success("Tack för att du hjälper till att minska vattenförbrukningen!")

    # Förslag 3
    with st.expander("🔧 Se över läckande kranar och toaletter"):
     #   st.image("https://example.com/leak.jpg", width=150)  # Ersätt med riktig bild-URL
        st.write("Läckande kranar och toaletter kan förlora mycket vatten varje dag. Kontrollera dina installationsenheter.")
        
        leaks_per_month = st.slider(
            "Hur många läckor har du åtgärdat?", 
            min_value=0, 
            max_value=10, 
            value=1, 
            step=1,
            key="leaks_slider"
        )
        
        leak_liters_saved = leaks_per_month * 30  # Exempel: 30 liter per läcka per vecka
        st.write(f"Du sparar ungefär **{leak_liters_saved} liter vatten per månad** genom att åtgärda läckor.")

        if st.button("Jag har fixat eventuella läckor!"):
            st.success("Fint arbete! Varje liten förändring räknas!")

    # Förslag 4
    with st.expander("💦 Minimera vattenanvändning vid disk och tvätt"):
     #   st.image("https://example.com/diskmaskin.jpg", width=150)  # Ersätt med riktig bild-URL
        st.write("Använd alltid fulla tvätt- och diskmaskiner för att optimera vattenanvändningen.")
        
        machines_per_week = st.slider(
            "Hur många gånger använder du tvätt- eller diskmaskinen per vecka?", 
            min_value=1, 
            max_value=14, 
            value=7, 
            step=1,
            key="machines_slider"
        )
        
        machines_liters_saved = machines_per_week * 15  # Exempel: 15 liter per gång
        st.write(f"Du sparar ungefär **{machines_liters_saved} liter vatten per vecka** genom att använda fulla maskiner.")

        if st.button("Jag använder nu maskinerna mer effektivt!"):
            st.success("Toppen! Att minska användningen av små belastningar sparar både vatten och energi.")

    # Förslag 5
    with st.expander("🧴 Välj kortare tvättprogram i tvättmaskinen"):
     #   st.image("https://example.com/tvattmaskin.jpg", width=150)  # Ersätt med riktig bild-URL
        st.write("Försök att använda tvätt- och diskmaskiner med full last och välj ett kortare program när det är möjligt.")
        
        optimized_machines_slider = st.slider(
            "Hur ofta använder du kortare program?", 
            min_value=0, 
            max_value=7, 
            value=3, 
            step=1,
            key="optimized_machines_slider"
        )
        
        optimized_machines_liters_saved = optimized_machines_slider * 12  # Exempel: 12 liter per kort program
        st.write(f"Du sparar ungefär **{optimized_machines_liters_saved} liter vatten per vecka** genom att använda kortare program.")

        if st.button("Jag har optimerat mina tvättvanor!"):
            st.success("Fantastiskt! Dina åtgärder bidrar till en mer hållbar livsstil.")

    # Förslag 6
    with st.expander("🌿 Samla regnvatten för bevattning"):
      #  st.image("https://example.com/regnvatten.jpg", width=150)
        st.write("Har du en balkong? Då kan du samla regnvatten för att använda till bevattning av egna växter.")
        
        rainwater_usage = st.slider(
            "Hur mycket regnvatten samlar du varje vecka?", 
            min_value=0, 
            max_value=50, 
            value=10, 
            step=5,
            key="rainwater_slider"
        )
        
        st.write(f"Du sparar ungefär **{rainwater_usage * 10} liter vatten per vecka** genom att använda regnvatten för bevattning.")

    # Förslag 7
    with st.expander("🚰 Skölj förpackningen med diskvatten"):
       # st.image("https://example.com/vattensparande.jpg", width=150)
        st.write("Om du diskar för hand kan du använda diskvattnet som blir över för att skölja ur förpackningen.")
        
        products_used = st.slider(
            "Hur många vattensparande produkter har du installerat?", 
            min_value=0, 
            max_value=5, 
            value=2, 
            step=1,
            key="products_slider"
        )
        
        st.write(f"Du sparar ungefär **{products_used * 20} liter vatten per vecka** genom att använda vattensparande produkter.")

    # Förslag 8
    with st.expander("🌱 Vatten i kylskåpet"):
      #  st.image("https://example.com/vaxter.jpg", width=150)
        st.write("Fylla en tillbringare eller flaska med vatten och sätt in i kylen så slipper du spola länge i kranen för att få kallt vatten att dricka.")
        
        low_water_plants = st.slider(
            "Hur många växter med låg vattenbehov har du?", 
            min_value=0, 
            max_value=10, 
            value=5, 
            step=1,
            key="plants_slider"
        )
        
        st.write(f"Du sparar ungefär **{low_water_plants * 5} liter vatten per vecka** genom att odla växter med lågt vattenbehov.")

    # Förslag 9
    with st.expander("🌍 Diska inte under rinnande vatten"):
    #    st.image("https://example.com/ateranvand.jpg", width=150)
        st.write("Genom att inte diska under rinnande vatten kan du spara 50 l varje gång du diskar, vilket kan innebära 15 000 liter per år.")
        
        water_reused = st.slider(
            "Hur mycket vatten återanvänder du per vecka?", 
            min_value=0, 
            max_value=50, 
            value=15, 
            step=5,
            key="water_reused_slider"
        )
        
        st.write(f"Du sparar ungefär **{water_reused * 5} liter vatten per vecka** genom att återanvända vatten.")

    # Förslag 10
    with st.expander("🚪 Stäng av vattnet när du borstar tänderna"):
     #   st.image("https://example.com/tandborstning.jpg", width=150)
        st.write("Stäng av vattnet medan du borstar tänderna för att minska vattenanvändningen.")
        
        teeth_brushing_times = st.slider(
            "Hur ofta borstar du tänderna per vecka?", 
            min_value=0, 
            max_value=14, 
            value=7, 
            step=1,
            key="teeth_brushing_slider"
        )
        
        st.write(f"Du sparar ungefär **{teeth_brushing_times * 2} liter vatten per vecka** genom att stänga av vattnet under tandborstning.")

# Visa åtgärdsförslag
show_actions()
