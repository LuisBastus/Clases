





(: Consulta 2: Detalles del os albumes :)
<detallAlbums>{
  for $album in doc("xq.xml")/repositoriDeMusica/album
  return
    <info>
      <titol>{ $album/titol/text() }</titol>
      <anyPublicacio>{ $album/anyPublicacio/text() }</anyPublicacio>
    </info>
}</detallAlbums>




(: Consulta 3: Àlbums econòmics amb preu < 10 EUR :)
<albumsEconomics>{
  for $album in doc("xq.xml")/repositoriDeMusica/album
  where $album/preu/@moneda = "EUR" and xs:decimal($album/preu) < 10
  return
    <album>
      <titol>{ $album/titol/text() }</titol>
      <artista>{ $album/artista/text() }</artista>
    </album>
}</albumsEconomics>
