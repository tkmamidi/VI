from PyQt5.QtCore import Qt


def show_page(
    parsed_data, current_page, variant, gene, classification, prediction, prev_button, next_button
):
    variant.clear()
    gene.clear()
    classification.clear()
    prediction.clear()
    if parsed_data:
        page_data = list(parsed_data.values())[current_page]
        Variant_template, Gene_template, Classification_template, Predictions_template = template()
        variant_text = Variant_template.format(**page_data)
        gene_text = Gene_template.format(**page_data)
        classification_text = Classification_template.format(**page_data)
        prediction_text = Predictions_template.format(**page_data)
        variant.setHtml(variant_text)
        gene.setHtml(gene_text)
        classification.setHtml(classification_text)
        prediction.setHtml(prediction_text)

    prev_button.setEnabled(current_page > 0)
    next_button.setEnabled(current_page < len(parsed_data) - 1)


def template():
    Variant_template = """
<html>
<head>
<style>
h1 {{text-align: center;}}
p {{text-align: center;}}
div {{text-align: center;}}
</style>
</head>
<body>
        <div class="row">
            <h3>Variant Info</h3>
                <p>Chromosome: {Chromosome}</p>
                <p>Position: {Position}</p>
                <p>Ref Allele: {Ref Allele}</p>
                <p>Alt Allele: {Alt Allele}</p>
                <p>UCSC: <a
                    href="https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position={Chromosome}%3A{Position}%2D{Position}&hgsid=1605900055_lGHpROH21jdzM2N7zTud2ki7Ipv2">UCSC link</a></p>
            </div><br>
</body>
</html>
"""
    Gene_template = """
<html>
<head>
<style>
h1 {{text-align: center;}}
p {{text-align: center;}}
div {{text-align: center;}}
</style>
</head>
<body>
        <div class="row">
            <h3>Gene Info</h3>
                <p>Hugo Genename: <a
                    href="https://www.genecards.org/cgi-bin/carddisp.pl?gene={Hugo Genename}&keywords={Hugo Genename}">{Hugo Genename}</a></p>
                <p>Transcript: {Transcript}</p>
                <p>Consequence: {Consequence}</p>
                <p>HGVS: {HGVS}</p>
                <p>AA change: {AA change}</p>
            </div><br>
</body>
</html>
"""
    Classification_template = """
<html>
<head>
<style>
h1 {{text-align: center;}}
p {{text-align: center;}}
div {{text-align: center;}}
</style>
</head>
<body>

        <div class="row">
            <h3>Classification</h3>
                <p>Clinvar class: {Clinvar class}</p>
                <p>Clingen class: {Clingen class}</p>
            </div><br>

</body>
</html>
"""
    Predictions_template = """
<html>
<head>
<style>
h1 {{text-align: center;}}
p {{text-align: center;}}
div {{text-align: center;}}
</style>
</head>
<body>

        <div class="row">
            <h3>Predictions</h3>
                <p><b>Ditto score: {Ditto score}</b></p>
                <p>gnomAD AF:  <a
                    href="http://www.gnomad-sg.org/region/{Chromosome}-{Position}-{Position}?dataset=gnomad_r3">{gnomAD AF}</a></p>
                <p>GERP score: {GERP score}</p>
                <p>CADD score: {CADD score}</p>
                <p>Clinpred score: {Clinpred score}</p>
            </div><br>

</body>
</html>
"""
    return Variant_template, Gene_template, Classification_template, Predictions_template
