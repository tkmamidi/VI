def show_page(parsed_data, current_page, text, prev_button, next_button):
    text.clear()
    output_html = ""
    if parsed_data:
        page_data = list(parsed_data.values())[current_page]
        html_template = template()
        page_text = html_template.format(**page_data)
        text.setHtml(page_text)

    prev_button.setEnabled(current_page > 0)
    next_button.setEnabled(current_page < len(parsed_data) - 1)


def template():
    html_template = """

<div class="row">
    <div class="left-column"><h3>Variant Info</h3>
<p>Chromosome: {Chromosome}</p>
<p>Position: {Position}</p>
<p>Ref Allele: {Ref Allele}</p>
<p>Alt Allele: {Alt Allele}</p>
<p>UCSC: <a
href="https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position={Chromosome}%3A{Position}%2D{Position}&hgsid=1605900055_lGHpROH21jdzM2N7zTud2ki7Ipv2">UCSC link</a></p>
</div>
    <div class="right-column"><h3>Gene Info</h3>
<p>Hugo Genename: {Hugo Genename}</p>
<p>Transcript: {Transcript}</p>
<p>Consequence: {Consequence}</p>
<p>HGVS: {HGVS}</p>
<p>AA change: {AA change}</p>
</div>
</div>
<div class="row">
    <div class="left-column"><h3>Classification</h3>
<p>Clinvar class: {Clinvar class}</p>
<p>Clingen class: {Clingen class}</p>
</div>
    <div class="right-column"><h3>Predictions</h3>
<p>Ditto score: {Ditto score}</p>
<p>gnomAD AF: {gnomAD AF}</p>
<p>GERP score: {GERP score}</p>
<p>CADD score: {CADD score}</p>
<p>Clinpred score: {Clinpred score}</p>
</div>
</div>
<div class="row">
<div class="left-column"><h3>Analyst notes</h3>
<p>Notes: {notes}</p>
</div>
</div>

"""
    return html_template
