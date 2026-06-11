#!/usr/bin/env python3
"""
TidyMyMusic SEO Site Builder
Generates 1000+ keyword-targeted HTML pages + all essential site pages
Usage: python3 build.py
Output: ./dist/
"""

import os
import json
import re
from datetime import datetime, date

AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949052354004532&atid=tidymymusicweb"
SITE_NAME = "TidyMyMusic"
SITE_DOMAIN = "https://brightlane.github.io/tidymymusic"
BASE_PATH = "/tidymymusic"   # GitHub Pages subdirectory prefix
BUILD_DATE = date.today().isoformat()
DIST = "dist"

# ─────────────────────────────────────────────
# 1. KEYWORD DATABASE  (1000+ targeted phrases)
# ─────────────────────────────────────────────

# Each entry: (slug, keyword, category)
KEYWORDS = []

def kw(slug, keyword, cat):
    KEYWORDS.append({"slug": slug, "keyword": keyword, "cat": cat})

# ── Core product ──────────────────────────────
kw("tidymymusic", "TidyMyMusic", "brand")
kw("tidymymusic-download", "TidyMyMusic download", "brand")
kw("tidymymusic-free", "TidyMyMusic free", "brand")
kw("tidymymusic-free-trial", "TidyMyMusic free trial", "brand")
kw("tidymymusic-review", "TidyMyMusic review", "brand")
kw("tidymymusic-windows", "TidyMyMusic Windows", "brand")
kw("tidymymusic-mac", "TidyMyMusic Mac", "brand")
kw("tidymymusic-crack", "TidyMyMusic crack alternative", "brand")
kw("tidymymusic-license", "TidyMyMusic license key", "brand")
kw("tidymymusic-activation", "TidyMyMusic activation code", "brand")
kw("wondershare-tidymymusic", "Wondershare TidyMyMusic", "brand")
kw("wondershare-tidymymusic-review", "Wondershare TidyMyMusic review", "brand")
kw("wondershare-music-organizer", "Wondershare music organizer", "brand")
kw("tidymymusic-2025", "TidyMyMusic 2025", "brand")
kw("tidymymusic-latest-version", "TidyMyMusic latest version", "brand")
kw("tidymymusic-coupon", "TidyMyMusic coupon code", "brand")
kw("tidymymusic-discount", "TidyMyMusic discount", "brand")
kw("tidymymusic-price", "TidyMyMusic price", "brand")
kw("tidymymusic-vs-musicbrainz", "TidyMyMusic vs MusicBrainz Picard", "brand")
kw("tidymymusic-vs-mp3tag", "TidyMyMusic vs Mp3tag", "brand")
kw("tidymymusic-alternative", "TidyMyMusic alternative", "brand")
kw("tidymymusic-tutorial", "TidyMyMusic tutorial", "brand")
kw("tidymymusic-how-to-use", "how to use TidyMyMusic", "brand")

# ── Music library organizer ───────────────────
kw("music-library-organizer", "music library organizer", "organizer")
kw("best-music-library-organizer", "best music library organizer", "organizer")
kw("free-music-library-organizer", "free music library organizer", "organizer")
kw("music-library-organizer-windows", "music library organizer Windows", "organizer")
kw("music-library-organizer-mac", "music library organizer Mac", "organizer")
kw("music-library-organizer-software", "music library organizer software", "organizer")
kw("music-library-organizer-2025", "music library organizer 2025", "organizer")
kw("best-music-library-software", "best music library software", "organizer")
kw("music-collection-organizer", "music collection organizer", "organizer")
kw("music-collection-manager", "music collection manager", "organizer")
kw("music-collection-software", "music collection software", "organizer")
kw("digital-music-organizer", "digital music organizer", "organizer")
kw("digital-music-collection-software", "digital music collection software", "organizer")
kw("organize-digital-music", "organize digital music", "organizer")
kw("music-file-organizer", "music file organizer", "organizer")
kw("music-file-manager", "music file manager", "organizer")
kw("music-folder-organizer", "music folder organizer", "organizer")
kw("organize-music-folders", "organize music folders", "organizer")
kw("music-manager-software", "music manager software", "organizer")
kw("music-manager-software-2025", "music manager software 2025", "organizer")
kw("best-music-manager", "best music manager software", "organizer")
kw("music-catalog-software", "music catalog software", "organizer")
kw("music-cataloging-software", "music cataloging software", "organizer")
kw("music-database-software", "music database software", "organizer")
kw("personal-music-library-software", "personal music library software", "organizer")
kw("home-music-library-software", "home music library software", "organizer")

# ── iTunes ────────────────────────────────────
kw("itunes-library-organizer", "iTunes library organizer", "itunes")
kw("itunes-cleaner", "iTunes cleaner", "itunes")
kw("itunes-library-cleaner", "iTunes library cleaner", "itunes")
kw("itunes-music-organizer", "iTunes music organizer", "itunes")
kw("organize-itunes-library", "organize iTunes library", "itunes")
kw("clean-up-itunes-library", "clean up iTunes library", "itunes")
kw("fix-itunes-library", "fix iTunes library", "itunes")
kw("itunes-library-fix", "iTunes library fix", "itunes")
kw("itunes-tag-fixer", "iTunes tag fixer", "itunes")
kw("itunes-art-fixer", "iTunes album art fixer", "itunes")
kw("itunes-duplicate-remover", "iTunes duplicate remover", "itunes")
kw("itunes-duplicate-songs", "remove duplicate songs iTunes", "itunes")
kw("itunes-missing-artwork", "fix iTunes missing artwork", "itunes")
kw("itunes-unknown-artist", "fix iTunes unknown artist", "itunes")
kw("itunes-mislabeled-songs", "fix iTunes mislabeled songs", "itunes")
kw("itunes-library-cleanup", "iTunes library cleanup", "itunes")
kw("itunes-library-management", "iTunes library management", "itunes")
kw("itunes-metadata-editor", "iTunes metadata editor", "itunes")
kw("itunes-companion-app", "best iTunes companion app", "itunes")
kw("itunes-helper-software", "iTunes helper software", "itunes")
kw("itunes-optimization", "iTunes library optimization", "itunes")
kw("itunes-storage-saver", "iTunes storage saver", "itunes")
kw("reduce-itunes-library-size", "reduce iTunes library size", "itunes")
kw("itunes-library-windows", "iTunes library organizer Windows", "itunes")
kw("itunes-library-mac", "iTunes library organizer Mac", "itunes")

# ── ID3 tags ──────────────────────────────────
kw("id3-tag-fixer", "ID3 tag fixer", "tags")
kw("id3-tag-editor", "ID3 tag editor", "tags")
kw("id3-tag-editor-windows", "ID3 tag editor Windows", "tags")
kw("id3-tag-editor-mac", "ID3 tag editor Mac", "tags")
kw("id3-tag-editor-free", "free ID3 tag editor", "tags")
kw("id3-tag-software", "ID3 tag software", "tags")
kw("id3-tag-repair", "ID3 tag repair", "tags")
kw("id3-tag-batch-editor", "ID3 tag batch editor", "tags")
kw("id3v2-tag-editor", "ID3v2 tag editor", "tags")
kw("mp3-tag-editor", "MP3 tag editor", "tags")
kw("mp3-tag-editor-windows", "MP3 tag editor Windows", "tags")
kw("mp3-tag-editor-mac", "MP3 tag editor Mac", "tags")
kw("mp3-tag-editor-free", "free MP3 tag editor", "tags")
kw("mp3-tag-fixer", "MP3 tag fixer", "tags")
kw("mp3-tag-software", "MP3 tag software", "tags")
kw("mp3-metadata-editor", "MP3 metadata editor", "tags")
kw("music-tag-editor", "music tag editor", "tags")
kw("music-tag-fixer", "music tag fixer", "tags")
kw("music-tag-repair", "music tag repair", "tags")
kw("music-metadata-editor", "music metadata editor", "tags")
kw("music-metadata-fixer", "music metadata fixer", "tags")
kw("music-metadata-software", "music metadata software", "tags")
kw("fix-music-tags", "fix music tags", "tags")
kw("fix-music-tags-automatically", "fix music tags automatically", "tags")
kw("fix-music-tags-software", "fix music tags software", "tags")
kw("fix-mp3-tags", "fix MP3 tags", "tags")
kw("fix-audio-tags", "fix audio tags", "tags")
kw("fix-missing-tags", "fix missing music tags", "tags")
kw("fill-missing-tags", "fill missing music tags", "tags")
kw("fix-mislabeled-songs", "fix mislabeled songs", "tags")
kw("fix-song-names", "fix song names", "tags")
kw("fix-artist-names", "fix artist names music", "tags")
kw("fix-album-names", "fix album names music", "tags")
kw("fix-track-numbers", "fix track numbers music", "tags")
kw("fix-genre-tags", "fix genre tags music", "tags")
kw("fix-year-tags", "fix year tags music", "tags")
kw("fix-unknown-artist", "fix Unknown Artist music", "tags")
kw("fix-unknown-album", "fix Unknown Album music", "tags")
kw("fix-track-01", "fix Track 01 music name", "tags")
kw("auto-tag-music", "auto tag music", "tags")
kw("auto-tag-mp3", "auto tag MP3 files", "tags")
kw("automatic-music-tagging", "automatic music tagging", "tags")
kw("automatic-id3-tagger", "automatic ID3 tagger", "tags")
kw("bulk-music-tagger", "bulk music tagger", "tags")
kw("batch-mp3-tagger", "batch MP3 tagger", "tags")
kw("batch-music-tagger", "batch music tagger", "tags")
kw("batch-id3-tagger", "batch ID3 tagger", "tags")
kw("song-tagger-software", "song tagger software", "tags")
kw("song-metadata-fixer", "song metadata fixer", "tags")
kw("audio-tag-editor", "audio tag editor", "tags")
kw("audio-tag-repair", "audio tag repair", "tags")
kw("bulk-audio-tagger", "bulk audio tagger", "tags")
kw("music-label-organizer", "music label organizer", "tags")
kw("music-info-fixer", "music info fixer", "tags")
kw("complete-music-metadata", "complete music metadata", "tags")
kw("fill-music-metadata", "fill music metadata", "tags")
kw("music-meta-fixer", "music meta fixer", "tags")
kw("best-mp3-tagger", "best MP3 tagger", "tags")
kw("best-music-tagger", "best music tagger", "tags")

# ── Album art ─────────────────────────────────
kw("album-art-downloader", "album art downloader", "artwork")
kw("album-artwork-downloader", "album artwork downloader", "artwork")
kw("album-cover-downloader", "album cover downloader", "artwork")
kw("download-album-artwork", "download album artwork", "artwork")
kw("download-album-art-automatically", "download album art automatically", "artwork")
kw("fetch-album-covers", "fetch album covers automatically", "artwork")
kw("album-art-fixer", "album art fixer", "artwork")
kw("album-artwork-fixer", "album artwork fixer", "artwork")
kw("fix-missing-album-art", "fix missing album art", "artwork")
kw("fix-missing-artwork-itunes", "fix missing artwork iTunes", "artwork")
kw("embed-album-art-mp3", "embed album art MP3", "artwork")
kw("add-album-art-mp3", "add album art to MP3", "artwork")
kw("album-art-embedder", "album art embedder software", "artwork")
kw("high-resolution-album-art", "high resolution album art downloader", "artwork")
kw("album-art-for-itunes", "album art for iTunes", "artwork")
kw("missing-album-artwork-fixer", "missing album artwork fixer", "artwork")
kw("music-artwork-fixer", "music artwork fixer", "artwork")
kw("cover-art-downloader", "cover art downloader music", "artwork")
kw("automatic-album-art", "automatic album art download", "artwork")
kw("batch-album-art-downloader", "batch album art downloader", "artwork")

# ── Lyrics ────────────────────────────────────
kw("lyrics-downloader-mp3", "lyrics downloader for MP3", "lyrics")
kw("download-song-lyrics", "download song lyrics automatically", "lyrics")
kw("embed-lyrics-mp3", "embed lyrics in MP3 files", "lyrics")
kw("music-lyrics-software", "music lyrics software", "lyrics")
kw("lyrics-finder-software", "lyrics finder software", "lyrics")
kw("add-lyrics-to-mp3", "add lyrics to MP3 files", "lyrics")
kw("synchronized-lyrics-mp3", "synchronized lyrics MP3", "lyrics")
kw("lyrics-tagger-software", "lyrics tagger software", "lyrics")
kw("automatic-lyrics-download", "automatic lyrics download", "lyrics")
kw("batch-lyrics-downloader", "batch lyrics downloader", "lyrics")

# ── Duplicate removal ─────────────────────────
kw("duplicate-song-remover", "duplicate song remover", "duplicates")
kw("duplicate-song-remover-free", "free duplicate song remover", "duplicates")
kw("find-duplicate-songs", "find duplicate songs", "duplicates")
kw("remove-duplicate-songs", "remove duplicate songs", "duplicates")
kw("remove-duplicate-music", "remove duplicate music files", "duplicates")
kw("duplicate-music-finder", "duplicate music finder", "duplicates")
kw("duplicate-mp3-finder", "duplicate MP3 finder", "duplicates")
kw("duplicate-mp3-remover", "duplicate MP3 remover", "duplicates")
kw("itunes-duplicate-finder", "iTunes duplicate finder", "duplicates")
kw("free-up-music-storage", "free up music storage", "duplicates")
kw("music-disk-cleaner", "music disk cleaner", "duplicates")
kw("music-storage-optimizer", "music storage optimizer", "duplicates")
kw("delete-duplicate-songs", "delete duplicate songs automatically", "duplicates")
kw("music-deduplication-software", "music deduplication software", "duplicates")
kw("audio-duplicate-finder", "audio duplicate finder", "duplicates")

# ── Acoustic fingerprinting ───────────────────
kw("acoustic-fingerprint-music", "acoustic fingerprint music identification", "tech")
kw("music-fingerprinting-software", "music fingerprinting software", "tech")
kw("audio-fingerprinting-software", "audio fingerprinting software", "tech")
kw("song-identification-software", "song identification software", "tech")
kw("music-recognition-software", "music recognition software", "tech")
kw("automatic-song-identification", "automatic song identification", "tech")
kw("music-recognition-technology", "music recognition technology", "tech")
kw("identify-unknown-music", "identify unknown music files", "tech")
kw("identify-songs-automatically", "identify songs automatically", "tech")
kw("music-fingerprint-identifier", "music fingerprint identifier", "tech")

# ── File formats ──────────────────────────────
kw("mp3-organizer", "MP3 organizer", "format")
kw("mp3-file-organizer", "MP3 file organizer", "format")
kw("organize-mp3-files", "organize MP3 files", "format")
kw("mp3-library-organizer", "MP3 library organizer", "format")
kw("flac-organizer", "FLAC organizer", "format")
kw("flac-tagger", "FLAC tagger", "format")
kw("flac-metadata-editor", "FLAC metadata editor", "format")
kw("flac-tag-editor", "FLAC tag editor", "format")
kw("flac-library-organizer", "FLAC library organizer", "format")
kw("m4a-tagger", "M4A tagger", "format")
kw("m4a-tag-editor", "M4A tag editor", "format")
kw("m4a-organizer", "M4A organizer", "format")
kw("aac-tagger", "AAC tagger", "format")
kw("aac-organizer", "AAC organizer", "format")
kw("wav-organizer", "WAV organizer", "format")
kw("wav-tagger", "WAV tagger", "format")
kw("wma-tagger", "WMA tagger", "format")
kw("wma-organizer", "WMA organizer", "format")
kw("ogg-tagger", "OGG tagger", "format")
kw("aiff-tagger", "AIFF tagger", "format")
kw("multi-format-music-organizer", "multi-format music organizer", "format")
kw("all-format-music-tagger", "all format music tagger", "format")
kw("lossless-music-organizer", "lossless music organizer", "format")
kw("lossless-audio-tagger", "lossless audio tagger", "format")

# ── Platform / OS ─────────────────────────────
kw("music-organizer-windows-10", "music organizer Windows 10", "platform")
kw("music-organizer-windows-11", "music organizer Windows 11", "platform")
kw("music-organizer-windows-7", "music organizer Windows 7", "platform")
kw("music-organizer-windows-8", "music organizer Windows 8", "platform")
kw("music-organizer-macos", "music organizer macOS", "platform")
kw("music-organizer-mac-2025", "music organizer Mac 2025", "platform")
kw("music-organizer-macos-sequoia", "music organizer macOS Sequoia", "platform")
kw("music-organizer-macos-sonoma", "music organizer macOS Sonoma", "platform")
kw("music-organizer-macos-ventura", "music organizer macOS Ventura", "platform")
kw("music-organizer-macos-monterey", "music organizer macOS Monterey", "platform")
kw("music-organizer-macos-big-sur", "music organizer macOS Big Sur", "platform")
kw("music-organizer-macos-catalina", "music organizer macOS Catalina", "platform")
kw("music-tagger-windows", "music tagger Windows", "platform")
kw("music-tagger-mac", "music tagger Mac", "platform")
kw("desktop-music-organizer", "desktop music organizer", "platform")
kw("offline-music-organizer", "offline music organizer", "platform")
kw("local-music-organizer", "local music organizer", "platform")

# ── Device / sync ─────────────────────────────
kw("iphone-music-organizer", "iPhone music organizer", "device")
kw("ipad-music-organizer", "iPad music organizer", "device")
kw("ipod-music-organizer", "iPod music organizer", "device")
kw("sync-music-to-iphone", "sync music to iPhone organized", "device")
kw("music-for-iphone-organizer", "music organizer for iPhone sync", "device")
kw("android-music-organizer", "Android music organizer", "device")
kw("mobile-music-organizer", "mobile music organizer", "device")
kw("transfer-music-to-iphone", "transfer organized music to iPhone", "device")
kw("nas-music-organizer", "NAS music organizer", "device")
kw("network-music-organizer", "network music organizer", "device")
kw("home-media-server-music", "home media server music organizer", "device")
kw("plex-music-metadata", "Plex music metadata organizer", "device")
kw("jellyfin-music-tags", "Jellyfin music tags organizer", "device")
kw("navidrome-music-organizer", "Navidrome music organizer", "device")
kw("kodi-music-organizer", "Kodi music organizer", "device")

# ── Use cases ─────────────────────────────────
kw("how-to-organize-music-library", "how to organize music library", "howto")
kw("best-way-to-organize-music", "best way to organize music", "howto")
kw("how-to-fix-music-tags", "how to fix music tags", "howto")
kw("how-to-add-album-art-mp3", "how to add album art to MP3", "howto")
kw("how-to-remove-duplicate-songs", "how to remove duplicate songs", "howto")
kw("how-to-organize-itunes", "how to organize iTunes library", "howto")
kw("how-to-fix-unknown-artist", "how to fix Unknown Artist in iTunes", "howto")
kw("how-to-embed-album-art", "how to embed album art in music files", "howto")
kw("how-to-download-lyrics-mp3", "how to download lyrics for MP3", "howto")
kw("how-to-clean-music-library", "how to clean music library", "howto")
kw("how-to-batch-tag-music", "how to batch tag music files", "howto")
kw("how-to-fix-music-metadata", "how to fix music metadata", "howto")
kw("how-to-identify-unknown-songs", "how to identify unknown songs", "howto")
kw("how-to-sort-music-by-artist", "how to sort music by artist", "howto")
kw("how-to-sort-music-by-album", "how to sort music by album", "howto")
kw("how-to-rename-music-files", "how to rename music files automatically", "howto")
kw("how-to-fix-flac-tags", "how to fix FLAC tags", "howto")
kw("how-to-organize-mp3-collection", "how to organize MP3 collection", "howto")
kw("how-to-fix-music-after-ripping", "how to fix music tags after ripping CD", "howto")
kw("how-to-transfer-music-iphone", "how to transfer music to iPhone with correct tags", "howto")

# ── Audience / use case ───────────────────────
kw("audiophile-music-organizer", "audiophile music organizer", "audience")
kw("dj-music-organizer", "DJ music organizer software", "audience")
kw("music-producer-organizer", "music producer library organizer", "audience")
kw("vinyl-rip-organizer", "vinyl rip organizer software", "audience")
kw("cd-rip-organizer", "CD rip music organizer", "audience")
kw("digitized-music-organizer", "digitized music organizer", "audience")
kw("music-archive-software", "music archive software", "audience")
kw("home-studio-music-organizer", "home studio music organizer", "audience")
kw("music-teacher-organizer", "music teacher library organizer", "audience")
kw("music-lover-software", "music lover software", "audience")
kw("gift-for-music-lover", "gift for music lover software", "audience")
kw("music-fan-organizer", "music fan organizer", "audience")
kw("large-music-library-organizer", "large music library organizer", "audience")
kw("small-music-collection-organizer", "small music collection organizer", "audience")
kw("casual-music-listener-organizer", "casual music listener organizer", "audience")

# ── Genre-specific ───────────────────────────
kw("classical-music-organizer", "classical music library organizer", "genre")
kw("jazz-music-organizer", "jazz music library organizer", "genre")
kw("rock-music-organizer", "rock music library organizer", "genre")
kw("hip-hop-music-organizer", "hip hop music library organizer", "genre")
kw("edm-music-organizer", "EDM music library organizer", "genre")
kw("country-music-organizer", "country music library organizer", "genre")
kw("pop-music-organizer", "pop music library organizer", "genre")
kw("metal-music-organizer", "metal music library organizer", "genre")
kw("indie-music-organizer", "indie music library organizer", "genre")
kw("rnb-music-organizer", "R&B music library organizer", "genre")
kw("soul-music-organizer", "soul music library organizer", "genre")
kw("blues-music-organizer", "blues music library organizer", "genre")
kw("reggae-music-organizer", "reggae music library organizer", "genre")
kw("folk-music-organizer", "folk music library organizer", "genre")
kw("opera-music-organizer", "opera music library organizer", "genre")
kw("orchestral-music-organizer", "orchestral music library organizer", "genre")
kw("world-music-organizer", "world music library organizer", "genre")
kw("electronic-music-organizer", "electronic music library organizer", "genre")
kw("soundtrack-organizer", "film soundtrack organizer", "genre")
kw("video-game-music-organizer", "video game music organizer", "genre")
kw("christmas-music-organizer", "Christmas music library organizer", "genre")
kw("gospel-music-organizer", "gospel music library organizer", "genre")

# ── Competitor comparisons ────────────────────
kw("vs-mp3tag", "TidyMyMusic vs Mp3tag", "compare")
kw("vs-musicbrainz-picard", "TidyMyMusic vs MusicBrainz Picard", "compare")
kw("vs-beets", "TidyMyMusic vs Beets music organizer", "compare")
kw("vs-bliss", "TidyMyMusic vs Bliss music organizer", "compare")
kw("vs-mediamonkey", "TidyMyMusic vs MediaMonkey", "compare")
kw("vs-foobar2000", "TidyMyMusic vs foobar2000", "compare")
kw("vs-itunes-builtin", "TidyMyMusic vs iTunes built-in tagging", "compare")
kw("vs-tuneup", "TidyMyMusic vs TuneUp", "compare")
kw("mp3tag-alternative", "Mp3tag alternative", "compare")
kw("musicbrainz-alternative", "MusicBrainz Picard alternative", "compare")
kw("mediamonkey-alternative", "MediaMonkey alternative", "compare")
kw("best-mp3tag-alternative", "best Mp3tag alternative Windows", "compare")
kw("best-music-tagger-2025", "best music tagger 2025", "compare")
kw("best-music-organizer-2025", "best music organizer software 2025", "compare")
kw("top-music-organizer-software", "top music organizer software", "compare")
kw("music-organizer-comparison", "music organizer software comparison", "compare")

# ── Global / language ─────────────────────────
kw("music-organizer-uk", "music organizer software UK", "global")
kw("music-organizer-australia", "music organizer software Australia", "global")
kw("music-organizer-canada", "music organizer software Canada", "global")
kw("music-organizer-germany", "Musikbibliothek organisieren Software", "global")
kw("music-organizer-france", "logiciel organisateur musique", "global")
kw("music-organizer-spain", "organizador biblioteca música", "global")
kw("music-organizer-italy", "organizzatore libreria musicale", "global")
kw("music-organizer-japan", "音楽ライブラリ整理ソフト", "global")
kw("music-organizer-brazil", "organizador biblioteca musical", "global")
kw("music-organizer-india", "music library organizer India", "global")
kw("music-organizer-netherlands", "muziekbibliotheek organizer", "global")
kw("music-organizer-sweden", "musikbibliotek organisera", "global")
kw("music-organizer-poland", "organizator biblioteki muzycznej", "global")
kw("music-organizer-russia", "организатор музыкальной библиотеки", "global")
kw("music-organizer-korea", "음악 라이브러리 정리 소프트웨어", "global")
kw("music-organizer-china", "音乐库管理软件", "global")
kw("music-organizer-mexico", "organizador de música Mexico", "global")
kw("music-organizer-argentina", "organizador música Argentina", "global")
kw("music-organizer-south-africa", "music organizer South Africa", "global")
kw("music-organizer-new-zealand", "music organizer New Zealand", "global")
kw("international-music-organizer", "international music organizer software", "global")
kw("global-music-library-tool", "global music library management tool", "global")

# ── Batch / automation ────────────────────────
kw("batch-music-organizer", "batch music organizer", "batch")
kw("batch-audio-organizer", "batch audio file organizer", "batch")
kw("batch-rename-music-files", "batch rename music files", "batch")
kw("bulk-rename-music", "bulk rename music files", "batch")
kw("bulk-tag-music", "bulk tag music files", "batch")
kw("batch-fix-music-tags", "batch fix music tags", "batch")
kw("one-click-music-organizer", "one click music organizer", "batch")
kw("automatic-music-organization", "automatic music organization software", "batch")
kw("smart-music-organizer", "smart music organizer", "batch")
kw("ai-music-organizer", "AI music organizer", "batch")
kw("intelligent-music-tagger", "intelligent music tagger", "batch")

# ── Storage / cleanup ─────────────────────────
kw("music-storage-cleaner", "music storage cleaner", "storage")
kw("free-up-hard-drive-music", "free up hard drive space music", "storage")
kw("music-library-size-reducer", "music library size reducer", "storage")
kw("remove-junk-music-files", "remove junk music files", "storage")
kw("optimize-music-storage", "optimize music storage", "storage")
kw("music-cleanup-tool", "music cleanup tool", "storage")
kw("clean-music-library", "clean music library software", "storage")
kw("music-library-maintenance", "music library maintenance software", "storage")

# ── Sorting / browsing ───────────────────────
kw("sort-music-by-artist", "sort music by artist automatically", "sorting")
kw("sort-music-by-album", "sort music by album automatically", "sorting")
kw("sort-music-by-genre", "sort music by genre automatically", "sorting")
kw("sort-music-by-year", "sort music by year automatically", "sorting")
kw("music-library-sort", "music library sort software", "sorting")
kw("organize-music-by-artist", "organize music by artist", "sorting")
kw("organize-music-by-genre", "organize music by genre", "sorting")
kw("music-search-software", "music search software library", "sorting")
kw("browse-music-collection", "browse music collection software", "sorting")

# ── CD ripping / digitization ─────────────────
kw("cd-rip-tag-fixer", "fix CD rip music tags", "ripping")
kw("cd-ripper-tag-fixer", "CD ripper tag fixer", "ripping")
kw("fix-ripped-cd-tags", "fix ripped CD music tags", "ripping")
kw("music-rip-organizer", "music rip organizer", "ripping")
kw("vinyl-digitize-organizer", "vinyl digitize music organizer", "ripping")
kw("cassette-digitize-organizer", "cassette digitize music organizer", "ripping")
kw("digitize-music-collection", "digitize and organize music collection", "ripping")
kw("music-archive-organizer", "music archive organizer", "ripping")

# ── Migration ─────────────────────────────────
kw("migrate-music-library", "migrate music library software", "migration")
kw("music-library-migration", "music library migration tool", "migration")
kw("move-music-library", "move music library to new computer", "migration")
kw("transfer-music-library", "transfer music library", "migration")
kw("backup-music-library", "backup music library software", "migration")
kw("music-library-export", "music library export tool", "migration")
kw("music-library-import", "music library import software", "migration")

# ── Pricing / free tools ─────────────────────
kw("free-music-organizer", "free music organizer software", "pricing")
kw("free-music-organizer-download", "free music organizer download", "pricing")
kw("free-music-tagger", "free music tagger", "pricing")
kw("free-mp3-tagger", "free MP3 tagger download", "pricing")
kw("free-id3-tag-editor", "free ID3 tag editor", "pricing")
kw("music-organizer-free-trial", "music organizer free trial", "pricing")
kw("cheap-music-organizer", "cheap music organizer software", "pricing")
kw("affordable-music-organizer", "affordable music organizer", "pricing")
kw("best-free-music-organizer", "best free music organizer", "pricing")
kw("best-free-mp3-tagger", "best free MP3 tagger 2025", "pricing")

# ── Professional use ──────────────────────────
kw("professional-music-organizer", "professional music organizer software", "pro")
kw("professional-music-library", "professional music library software", "pro")
kw("music-organizer-pro", "music organizer pro", "pro")
kw("music-tagger-professional", "music tagger professional", "pro")
kw("music-metadata-professional", "music metadata professional software", "pro")
kw("music-organizer-enterprise", "music organizer enterprise", "pro")
kw("music-library-enterprise", "music library enterprise software", "pro")

# ── Additional long-tail ──────────────────────
kw("music-organizer-8000-songs", "music organizer for 8000 songs", "longtail")
kw("music-organizer-10000-songs", "music organizer for 10000 songs", "longtail")
kw("music-organizer-50000-songs", "music organizer for 50000 songs", "longtail")
kw("music-organizer-large-collection", "music organizer large collection", "longtail")
kw("fix-itunes-after-reinstall", "fix iTunes library after reinstall", "longtail")
kw("music-library-after-hard-drive-crash", "restore music library after hard drive crash", "longtail")
kw("fix-music-after-format", "fix music tags after computer format", "longtail")
kw("music-organizer-for-beginners", "music organizer for beginners", "longtail")
kw("easiest-music-organizer", "easiest music organizer software", "longtail")
kw("music-organizer-no-technical-skills", "music organizer no technical skills needed", "longtail")
kw("fix-music-tags-without-internet", "fix music tags without internet", "longtail")
kw("music-organizer-with-lyrics", "music organizer with lyrics downloader", "longtail")
kw("music-organizer-with-artwork", "music organizer with artwork downloader", "longtail")
kw("all-in-one-music-organizer", "all in one music organizer", "longtail")
kw("complete-music-library-solution", "complete music library solution", "longtail")
kw("music-organizer-that-works", "music organizer that actually works", "longtail")
kw("best-itunes-alternative-organizer", "best iTunes alternative music organizer", "longtail")
kw("music-library-spring-clean", "music library spring clean software", "longtail")
kw("tidy-music-collection", "tidy music collection software", "longtail")
kw("organize-messy-music-library", "organize messy music library", "longtail")
kw("music-organizer-trustworthy", "trustworthy music organizer software", "longtail")
kw("wondershare-music-software", "Wondershare music software", "longtail")
kw("music-library-app-desktop", "music library app desktop", "longtail")
kw("music-tagger-that-uses-fingerprint", "music tagger that uses audio fingerprint", "longtail")
kw("music-organizer-embed-tags-in-file", "music organizer that embeds tags in file", "longtail")
kw("music-organizer-iphone-compatible", "music organizer iPhone compatible", "longtail")
kw("fix-music-sync-to-phone", "fix music before syncing to phone", "longtail")
kw("best-music-cleanup-software", "best music cleanup software", "longtail")
kw("music-organizer-trusted-software", "trusted music organizer software", "longtail")
kw("safe-music-organizer", "safe music organizer software", "longtail")
kw("music-collection-cleanup", "music collection cleanup tool", "longtail")
kw("music-files-mess-fix", "fix messy music files automatically", "longtail")

# ── Extended brand / product ──────────────────
kw("tidymymusic-windows-10", "TidyMyMusic Windows 10", "brand")
kw("tidymymusic-windows-11", "TidyMyMusic Windows 11", "brand")
kw("tidymymusic-macos", "TidyMyMusic macOS", "brand")
kw("tidymymusic-itunes", "TidyMyMusic iTunes", "brand")
kw("tidymymusic-iphone", "TidyMyMusic iPhone sync", "brand")
kw("tidymymusic-flac", "TidyMyMusic FLAC support", "brand")
kw("tidymymusic-mp3", "TidyMyMusic MP3", "brand")
kw("tidymymusic-safe", "is TidyMyMusic safe", "brand")
kw("tidymymusic-legit", "is TidyMyMusic legit", "brand")
kw("tidymymusic-worth-it", "is TidyMyMusic worth it", "brand")
kw("tidymymusic-buy", "buy TidyMyMusic", "brand")
kw("tidymymusic-install", "how to install TidyMyMusic", "brand")
kw("tidymymusic-uninstall", "how to uninstall TidyMyMusic", "brand")
kw("tidymymusic-update", "TidyMyMusic update", "brand")
kw("tidymymusic-support", "TidyMyMusic support", "brand")
kw("tidymymusic-for-windows", "TidyMyMusic for Windows", "brand")
kw("tidymymusic-for-mac", "TidyMyMusic for Mac", "brand")
kw("wondershare-tidymymusic-windows", "Wondershare TidyMyMusic Windows download", "brand")
kw("wondershare-tidymymusic-mac", "Wondershare TidyMyMusic Mac download", "brand")
kw("tidymymusic-vs-beets", "TidyMyMusic vs Beets", "brand")
kw("tidymymusic-features", "TidyMyMusic features list", "brand")
kw("tidymymusic-pros-cons", "TidyMyMusic pros and cons", "brand")

# ── Extended tag topics ───────────────────────
kw("fix-composer-tags", "fix composer tags music", "tags")
kw("fix-conductor-tags", "fix conductor tags classical music", "tags")
kw("fix-comment-tags", "fix comment tags MP3", "tags")
kw("fix-bpm-tags", "fix BPM tags music", "tags")
kw("fix-key-tags", "fix music key tags", "tags")
kw("fix-disc-number-tags", "fix disc number tags music", "tags")
kw("fix-compilation-tags", "fix compilation album tags", "tags")
kw("rewrite-music-tags", "rewrite music tags software", "tags")
kw("overwrite-music-tags", "overwrite music tags automatically", "tags")
kw("clean-music-tags", "clean music tags software", "tags")
kw("standardize-music-tags", "standardize music tags", "tags")
kw("normalize-music-tags", "normalize music tags software", "tags")
kw("music-tag-validator", "music tag validator software", "tags")
kw("music-tag-checker", "music tag checker", "tags")
kw("music-info-software", "music info software", "tags")
kw("music-info-editor", "music info editor", "tags")
kw("music-info-lookup", "music info lookup software", "tags")
kw("song-info-software", "song info software", "tags")
kw("song-info-editor", "song info editor", "tags")
kw("song-info-lookup", "song info lookup", "tags")
kw("track-info-fixer", "track info fixer software", "tags")
kw("track-info-editor", "track info editor", "tags")
kw("music-tagger-free-windows", "free music tagger Windows", "tags")
kw("music-tagger-free-mac", "free music tagger Mac", "tags")
kw("best-music-tagger-free", "best free music tagger software", "tags")
kw("music-tagging-software-free", "free music tagging software", "tags")
kw("automatic-music-tagger-free", "free automatic music tagger", "tags")

# ── Extended artwork ──────────────────────────
kw("album-art-recovery-software", "album art recovery software", "artwork")
kw("bulk-album-art-fixer", "bulk album art fixer", "artwork")
kw("automatic-cover-art", "automatic cover art download", "artwork")
kw("find-album-art-software", "find album art software", "artwork")
kw("get-album-art-automatically", "get album art automatically", "artwork")
kw("restore-album-art", "restore album art music library", "artwork")
kw("repair-album-art", "repair album art music", "artwork")
kw("replace-album-art", "replace album art software", "artwork")
kw("update-album-art", "update album art software", "artwork")
kw("embed-cover-art-flac", "embed cover art in FLAC files", "artwork")
kw("embed-cover-art-m4a", "embed cover art in M4A files", "artwork")
kw("album-cover-fixer-software", "album cover fixer software", "artwork")
kw("missing-cover-art-fixer", "missing cover art fixer", "artwork")
kw("best-album-art-downloader", "best album art downloader 2025", "artwork")
kw("free-album-art-downloader", "free album art downloader", "artwork")

# ── Extended iTunes ───────────────────────────
kw("itunes-library-fixer", "iTunes library fixer software", "itunes")
kw("itunes-music-fixer", "iTunes music fixer", "itunes")
kw("fix-itunes-tags-automatically", "fix iTunes tags automatically", "itunes")
kw("itunes-tag-repair-software", "iTunes tag repair software", "itunes")
kw("itunes-album-art-software", "iTunes album art software", "itunes")
kw("clean-itunes-music", "clean iTunes music", "itunes")
kw("tidy-itunes-library", "tidy iTunes library", "itunes")
kw("sort-itunes-library", "sort iTunes library automatically", "itunes")
kw("organize-itunes-music-mac", "organize iTunes music on Mac", "itunes")
kw("organize-itunes-music-windows", "organize iTunes music on Windows", "itunes")
kw("fix-itunes-music-info", "fix iTunes music information", "itunes")
kw("itunes-library-repair-tool", "iTunes library repair tool", "itunes")
kw("itunes-missing-info-fixer", "iTunes missing info fixer", "itunes")
kw("itunes-song-info-fixer", "iTunes song info fixer", "itunes")
kw("itunes-playlist-organizer", "iTunes playlist organizer", "itunes")
kw("itunes-library-consolidator", "iTunes library consolidator software", "itunes")

# ── Extended platform ─────────────────────────
kw("music-tagger-windows-10", "music tagger Windows 10", "platform")
kw("music-tagger-windows-11", "music tagger Windows 11", "platform")
kw("music-tagger-windows-7", "music tagger Windows 7", "platform")
kw("music-tagger-macos-sonoma", "music tagger macOS Sonoma", "platform")
kw("music-tagger-macos-ventura", "music tagger macOS Ventura", "platform")
kw("music-organizer-apple-silicon", "music organizer Apple Silicon Mac", "platform")
kw("music-organizer-m1-mac", "music organizer M1 Mac", "platform")
kw("music-organizer-m2-mac", "music organizer M2 Mac", "platform")
kw("music-organizer-m3-mac", "music organizer M3 Mac", "platform")
kw("music-organizer-intel-mac", "music organizer Intel Mac", "platform")
kw("music-manager-windows-10", "music manager Windows 10", "platform")
kw("music-manager-windows-11", "music manager Windows 11", "platform")
kw("music-manager-mac", "music manager Mac software", "platform")
kw("music-library-windows", "music library software Windows", "platform")
kw("music-library-mac", "music library software Mac", "platform")

# ── Extended duplicates ───────────────────────
kw("duplicate-audio-files", "find and remove duplicate audio files", "duplicates")
kw("duplicate-music-cleaner", "duplicate music cleaner software", "duplicates")
kw("free-duplicate-music-finder", "free duplicate music finder", "duplicates")
kw("best-duplicate-song-finder", "best duplicate song finder", "duplicates")
kw("automatic-duplicate-remover", "automatic duplicate song remover", "duplicates")
kw("smart-duplicate-finder", "smart duplicate music finder", "duplicates")
kw("music-deduplicator", "music deduplicator software", "duplicates")
kw("audio-deduplicator", "audio deduplicator software", "duplicates")
kw("remove-extra-music-copies", "remove extra music file copies", "duplicates")
kw("clean-duplicate-music", "clean duplicate music files", "duplicates")

# ── Extended tech ─────────────────────────────
kw("music-id-technology", "music identification technology", "tech")
kw("shazam-like-desktop-software", "Shazam-like desktop music software", "tech")
kw("music-recognition-desktop", "music recognition desktop software", "tech")
kw("identify-music-by-sound", "identify music by sound software", "tech")
kw("music-lookup-software", "music lookup software", "tech")
kw("music-database-lookup", "music database lookup software", "tech")
kw("music-info-lookup-software", "music info lookup software", "tech")
kw("automatic-music-recognition", "automatic music recognition software", "tech")
kw("content-based-music-retrieval", "content based music retrieval software", "tech")
kw("music-fingerprint-database", "music fingerprint database software", "tech")

# ── How-to extended ───────────────────────────
kw("how-to-fix-flac-metadata", "how to fix FLAC metadata", "howto")
kw("how-to-batch-download-album-art", "how to batch download album art", "howto")
kw("how-to-find-duplicate-songs-mac", "how to find duplicate songs on Mac", "howto")
kw("how-to-find-duplicate-songs-windows", "how to find duplicate songs on Windows", "howto")
kw("how-to-organize-music-windows-10", "how to organize music on Windows 10", "howto")
kw("how-to-organize-music-mac", "how to organize music on Mac", "howto")
kw("how-to-fix-music-after-migration", "how to fix music tags after PC migration", "howto")
kw("how-to-sync-music-iphone-correctly", "how to sync music to iPhone correctly", "howto")
kw("how-to-add-lyrics-itunes", "how to add lyrics to iTunes automatically", "howto")
kw("how-to-fix-compilation-album-tags", "how to fix compilation album tags", "howto")
kw("how-to-tag-classical-music", "how to tag classical music properly", "howto")
kw("how-to-tag-jazz-music", "how to tag jazz music library", "howto")
kw("how-to-clean-up-music-before-selling-pc", "how to clean up music before selling PC", "howto")
kw("how-to-back-up-music-library", "how to back up music library", "howto")
kw("how-to-move-itunes-to-new-computer", "how to move iTunes to new computer", "howto")
kw("how-to-fix-music-on-android", "how to fix music tags on Android", "howto")
kw("how-to-use-music-organizer-software", "how to use music organizer software", "howto")
kw("how-to-identify-songs-no-tags", "how to identify songs with no tags", "howto")
kw("how-to-complete-music-collection", "how to complete a music collection", "howto")
kw("how-to-fix-music-ripped-from-cd", "how to fix music ripped from CD without internet", "howto")

# ── Extended global ───────────────────────────
kw("music-organizer-europe", "music organizer Europe", "global")
kw("music-organizer-asia", "music organizer Asia", "global")
kw("music-organizer-latin-america", "music organizer Latin America", "global")
kw("music-organizer-middle-east", "music organizer Middle East", "global")
kw("music-organizer-africa", "music organizer Africa", "global")
kw("best-music-organizer-uk", "best music organizer UK 2025", "global")
kw("best-music-organizer-australia", "best music organizer Australia", "global")
kw("best-music-organizer-canada", "best music organizer Canada", "global")
kw("music-software-english", "music organizer software English", "global")
kw("music-software-multilingual", "multilingual music organizer software", "global")
kw("international-music-library-tool", "international music library tool", "global")
kw("music-organizer-worldwide", "music organizer available worldwide", "global")

# ── Extended sorting ──────────────────────────
kw("sort-music-by-decade", "sort music by decade", "sorting")
kw("sort-music-by-composer", "sort music by composer", "sorting")
kw("sort-music-by-conductor", "sort music by conductor", "sorting")
kw("sort-music-by-label", "sort music by record label", "sorting")
kw("sort-music-by-bitrate", "sort music by bitrate", "sorting")
kw("sort-music-by-format", "sort music by format", "sorting")
kw("sort-music-alphabetically", "sort music alphabetically software", "sorting")
kw("music-folder-structure-organizer", "music folder structure organizer", "sorting")
kw("automatic-music-folder-organizer", "automatic music folder organizer", "sorting")
kw("music-library-browse-software", "music library browsing software", "sorting")

# ── Extended storage ──────────────────────────
kw("reclaim-disk-space-music", "reclaim disk space from music library", "storage")
kw("music-storage-audit", "music storage audit software", "storage")
kw("find-large-music-files", "find large music files software", "storage")
kw("music-file-size-reducer", "music file size optimizer", "storage")
kw("clean-junk-music-files", "clean junk music files", "storage")
kw("remove-empty-music-folders", "remove empty music folders software", "storage")
kw("music-library-housekeeping", "music library housekeeping software", "storage")

# ── Extended audience ─────────────────────────
kw("music-organizer-collector", "music organizer for collectors", "audience")
kw("music-organizer-podcaster", "podcast and music organizer", "audience")
kw("music-organizer-radio-presenter", "radio presenter music organizer", "audience")
kw("music-organizer-content-creator", "content creator music organizer", "audience")
kw("music-organizer-gamer", "gamer music organizer", "audience")
kw("music-organizer-gym", "gym playlist music organizer", "audience")
kw("music-organizer-long-commute", "music organizer for long commutes", "audience")
kw("music-organizer-road-trip", "road trip music organizer", "audience")
kw("music-organizer-traveller", "traveller music organizer", "audience")
kw("music-organizer-retiree", "retiree music collection organizer", "audience")
kw("music-organizer-parent", "parent music library organizer", "audience")
kw("music-organizer-student", "student music library organizer", "audience")

# ── Extended genre ───────────────────────────
kw("ambient-music-organizer", "ambient music organizer", "genre")
kw("new-age-music-organizer", "new age music organizer", "genre")
kw("alternative-music-organizer", "alternative music organizer", "genre")
kw("punk-music-organizer", "punk music organizer", "genre")
kw("latin-music-organizer", "Latin music organizer", "genre")
kw("afrobeats-music-organizer", "Afrobeats music organizer", "genre")
kw("kpop-music-organizer", "K-pop music organizer", "genre")
kw("jpop-music-organizer", "J-pop music organizer", "genre")
kw("bollywood-music-organizer", "Bollywood music organizer", "genre")
kw("classical-tag-fixer", "classical music tag fixer", "genre")
kw("jazz-tag-fixer", "jazz music tag fixer", "genre")
kw("film-score-organizer", "film score music organizer", "genre")
kw("anime-music-organizer", "anime music organizer", "genre")
kw("podcast-audio-organizer", "podcast audio organizer", "genre")
kw("audiobook-organizer", "audiobook organizer software", "genre")

# ── Extended compare ─────────────────────────
kw("vs-winamp", "TidyMyMusic vs Winamp", "compare")
kw("vs-vlc-tagger", "TidyMyMusic vs VLC tagger", "compare")
kw("vs-clementine", "TidyMyMusic vs Clementine music player", "compare")
kw("vs-rhythmbox", "TidyMyMusic vs Rhythmbox", "compare")
kw("vs-banshee", "TidyMyMusic vs Banshee", "compare")
kw("vs-jaikoz", "TidyMyMusic vs Jaikoz", "compare")
kw("vs-kid3", "TidyMyMusic vs Kid3", "compare")
kw("vs-easytag", "TidyMyMusic vs EasyTag", "compare")
kw("best-alternative-to-mp3tag", "best alternative to Mp3tag", "compare")
kw("free-alternative-to-mediamonkey", "free alternative to MediaMonkey", "compare")
kw("best-music-organizer-vs-manual", "best music organizer vs manual tagging", "compare")
kw("beets-alternative", "Beets music organizer alternative", "compare")
kw("jaikoz-alternative", "Jaikoz alternative", "compare")
kw("kid3-alternative", "Kid3 alternative Windows Mac", "compare")
kw("picard-alternative", "MusicBrainz Picard alternative easier", "compare")
kw("easytag-alternative-windows", "EasyTag alternative Windows", "compare")

# ── Extended migration ───────────────────────
kw("import-music-to-itunes", "import music to iTunes automatically tagged", "migration")
kw("export-itunes-library", "export iTunes library organized", "migration")
kw("migrate-itunes-to-new-mac", "migrate iTunes to new Mac", "migration")
kw("migrate-itunes-to-new-pc", "migrate iTunes to new Windows PC", "migration")
kw("fix-music-after-pc-upgrade", "fix music tags after PC upgrade", "migration")
kw("fix-music-after-hard-drive-change", "fix music after changing hard drive", "migration")
kw("restore-music-library-backup", "restore music library from backup", "migration")
kw("consolidate-music-library", "consolidate music library software", "migration")

# ── Extended ripping ─────────────────────────
kw("fix-cddb-tags", "fix CDDB CD rip tags", "ripping")
kw("fix-gracenote-tags", "fix Gracenote CD tags", "ripping")
kw("retag-cd-rips", "retag CD rips software", "ripping")
kw("fix-multi-disc-album-tags", "fix multi-disc album tags", "ripping")
kw("fix-live-album-tags", "fix live album tags", "ripping")
kw("tag-bootleg-recordings", "tag bootleg recording software", "ripping")
kw("fix-cassette-digitization-tags", "fix cassette digitization tags", "ripping")

# ── Extended formats ──────────────────────────
kw("opus-tagger", "Opus audio tagger", "format")
kw("dsf-tagger", "DSD DSF tagger software", "format")
kw("alac-tagger", "Apple Lossless ALAC tagger", "format")
kw("mp4-audio-tagger", "MP4 audio tagger", "format")
kw("audiobook-m4b-tagger", "M4B audiobook tagger", "format")
kw("vorbis-tag-editor", "Vorbis tag editor software", "format")
kw("ape-tag-editor", "APE tag editor software", "format")
kw("id3v1-to-id3v2-converter", "ID3v1 to ID3v2 tag converter", "format")
kw("fix-encoding-tags", "fix music tag encoding errors", "format")
kw("unicode-music-tags", "Unicode music tags software", "format")

# ── Extended pricing ─────────────────────────
kw("music-organizer-under-40-dollars", "music organizer software under 40 dollars", "pricing")
kw("cheap-itunes-cleaner", "cheap iTunes cleaner software", "pricing")
kw("budget-music-organizer", "budget music organizer software", "pricing")
kw("one-time-purchase-music-organizer", "one-time purchase music organizer no subscription", "pricing")
kw("lifetime-license-music-organizer", "lifetime license music organizer", "pricing")
kw("music-organizer-no-subscription", "music organizer no subscription needed", "pricing")
kw("best-value-music-organizer", "best value music organizer software", "pricing")

# ── Extended device ───────────────────────────
kw("android-music-tag-fixer", "Android music tag fixer", "device")
kw("music-organizer-before-sync", "music organizer before device sync", "device")
kw("prepare-music-for-iphone-sync", "prepare music library for iPhone sync", "device")
kw("fix-music-before-android-sync", "fix music before Android sync", "device")
kw("music-organizer-car-stereo", "music organizer for car stereo USB", "device")
kw("music-organizer-usb-drive", "music organizer for USB drive", "device")
kw("music-organizer-mp3-player", "music organizer for MP3 player", "device")
kw("music-organizer-apple-watch", "music organizer Apple Watch sync", "device")
kw("music-for-plex-server", "organize music for Plex media server", "device")
kw("music-for-emby-server", "organize music for Emby server", "device")

# ── Extended batch ───────────────────────────
kw("mass-tag-music-files", "mass tag music files software", "batch")
kw("tag-music-in-bulk", "tag music files in bulk", "batch")
kw("fix-entire-music-library", "fix entire music library at once", "batch")
kw("auto-fix-music-collection", "auto fix music collection", "batch")
kw("automatic-library-fixer", "automatic music library fixer", "batch")
kw("music-cleanup-automation", "music library cleanup automation", "batch")
kw("scheduled-music-organizer", "scheduled music organizer software", "batch")

# ── Pro extended ─────────────────────────────
kw("music-organizer-for-studios", "music organizer for recording studios", "pro")
kw("music-organizer-for-labels", "music organizer for record labels", "pro")
kw("music-organizer-radio-stations", "music organizer for radio stations", "pro")
kw("music-organizer-broadcast", "music organizer for broadcast", "pro")
kw("music-organizer-filmmakers", "music organizer for filmmakers", "pro")
kw("music-organizer-game-developers", "music organizer for game developers", "pro")
kw("music-organizer-sound-designers", "music organizer for sound designers", "pro")

# ── Extended general ─────────────────────────
kw("music-organizer-app-2025", "best music organizer app 2025", "organizer")
kw("top-10-music-organizers", "top 10 music organizer software", "organizer")
kw("music-organisation-software", "music organisation software UK", "organizer")
kw("music-organization-tool", "music organization tool", "organizer")
kw("music-management-tool", "music management tool", "organizer")
kw("music-library-tool", "music library tool", "organizer")
kw("audio-library-organizer", "audio library organizer", "organizer")
kw("audio-collection-manager", "audio collection manager software", "organizer")
kw("sound-library-organizer", "sound library organizer software", "organizer")
kw("media-library-tagger", "media library tagger software", "organizer")
kw("media-file-tagger", "media file tagger software", "organizer")
kw("media-metadata-editor", "media metadata editor", "organizer")
kw("best-way-to-store-music", "best way to store digital music collection", "organizer")
kw("music-library-software-review", "music library software review 2025", "organizer")
kw("music-organization-guide", "music organization guide 2025", "organizer")
kw("tidy-music-library-guide", "tidy music library complete guide", "organizer")
kw("music-library-best-practices-2025", "music library best practices 2025", "organizer")
kw("how-to-start-organizing-music", "how to start organizing music collection", "organizer")
kw("music-library-from-scratch", "build organized music library from scratch", "organizer")
kw("rescue-messy-music-library", "rescue messy music library software", "organizer")

# ── 300 more to hit 1000+ ─────────────────────

# Music player integration
kw("foobar2000-music-organizer", "foobar2000 music organizer helper", "player")
kw("winamp-music-organizer", "Winamp music organizer", "player")
kw("musicbee-alternative", "MusicBee alternative organizer", "player")
kw("mediamonkey-free-alternative", "MediaMonkey free alternative", "player")
kw("clementine-music-tagger", "Clementine music tagger alternative", "player")
kw("vlc-music-tagger", "VLC music tagger alternative", "player")
kw("apple-music-organizer", "Apple Music library organizer", "player")
kw("spotify-local-music-organizer", "Spotify local files music organizer", "player")
kw("amazon-music-library-fix", "Amazon Music local library organizer", "player")
kw("tidal-local-music-organizer", "TIDAL local music organizer", "player")
kw("music-player-metadata-fixer", "music player metadata fixer", "player")
kw("windows-media-player-tagger", "Windows Media Player tag fixer", "player")
kw("groove-music-organizer", "Groove Music organizer Windows", "player")

# Specific problems
kw("fix-music-showing-wrong-artist", "fix music showing wrong artist name", "problem")
kw("fix-music-showing-wrong-album", "fix music showing wrong album name", "problem")
kw("fix-grey-artwork-itunes", "fix grey artwork iTunes", "problem")
kw("fix-no-album-art-showing", "fix no album art showing in music player", "problem")
kw("fix-duplicate-albums-itunes", "fix duplicate albums showing in iTunes", "problem")
kw("fix-songs-in-wrong-album", "fix songs appearing in wrong album", "problem")
kw("fix-split-album-itunes", "fix split album iTunes", "problem")
kw("fix-music-player-no-artwork", "fix music player not showing artwork", "problem")
kw("missing-genre-music-fix", "fix missing genre in music library", "problem")
kw("missing-year-music-fix", "fix missing year tag in music", "problem")
kw("fix-music-alphabetical-order", "fix music not sorting alphabetically", "problem")
kw("fix-music-not-showing-iphone", "fix music not showing on iPhone", "problem")
kw("fix-music-sync-error", "fix music sync error iTunes iPhone", "problem")
kw("fix-corrupted-music-tags", "fix corrupted music metadata tags", "problem")
kw("fix-blank-song-titles", "fix blank song titles in music library", "problem")
kw("fix-music-player-freezing", "fix music player freezing on untagged files", "problem")
kw("music-showing-as-unknown", "fix music showing as unknown in player", "problem")
kw("songs-out-of-order-fix", "fix songs playing out of order music", "problem")
kw("fix-track-numbers-wrong", "fix wrong track numbers in music player", "problem")
kw("fix-music-folder-mess", "fix messy music folder structure", "problem")

# Specific music library sizes
kw("organize-100-songs", "organize 100 songs music library", "size")
kw("organize-500-songs", "organize 500 songs collection", "size")
kw("organize-1000-songs", "organize 1000 songs music library", "size")
kw("organize-2000-songs", "organize 2000 songs collection", "size")
kw("organize-5000-songs", "organize 5000 songs music library", "size")
kw("organize-8000-songs", "organize 8000 songs collection", "size")
kw("organize-10000-songs", "organize 10000 songs music library", "size")
kw("organize-15000-songs", "organize 15000 songs collection", "size")
kw("organize-20000-songs", "organize 20000 songs music library", "size")
kw("organize-30000-songs", "organize 30000 songs collection", "size")
kw("organize-50000-songs", "organize 50000 songs music library", "size")
kw("music-library-1gb", "music library organizer 1GB collection", "size")
kw("music-library-10gb", "music library organizer 10GB collection", "size")
kw("music-library-100gb", "music library organizer 100GB collection", "size")
kw("music-library-1tb", "music library organizer 1TB collection", "size")

# Seasonal / promotional
kw("best-music-software-christmas-gift", "best music software Christmas gift", "seasonal")
kw("music-organizer-black-friday", "music organizer Black Friday deal", "seasonal")
kw("music-software-new-year-resolution", "music software new year resolution", "seasonal")
kw("music-organizer-summer-sale", "music organizer summer sale", "seasonal")
kw("music-software-gift-idea", "music software gift idea", "seasonal")
kw("music-lover-christmas-gift", "music lover Christmas gift software", "seasonal")
kw("best-software-for-music-fans", "best software for music fans 2025", "seasonal")

# Use case specific
kw("organize-itunes-before-switching-mac", "organize iTunes before switching Mac", "usecase")
kw("organize-music-before-selling-computer", "organize music before selling computer", "usecase")
kw("fix-music-after-windows-reinstall", "fix music library after Windows reinstall", "usecase")
kw("fix-music-after-macos-upgrade", "fix music library after macOS upgrade", "usecase")
kw("organize-inherited-music-collection", "organize inherited music collection", "usecase")
kw("organize-shared-family-music-library", "organize shared family music library", "usecase")
kw("organize-band-music-archive", "organize band music archive", "usecase")
kw("organize-church-music-library", "organize church music library software", "usecase")
kw("organize-school-music-library", "organize school music library software", "usecase")
kw("organize-fitness-studio-music", "organize fitness studio music library", "usecase")
kw("organize-restaurant-background-music", "organize restaurant background music", "usecase")
kw("organize-hotel-music-library", "organize hotel background music library", "usecase")
kw("fix-music-after-download", "fix music tags after downloading", "usecase")
kw("fix-music-from-torrent", "fix music tags from torrent downloads", "usecase")
kw("fix-music-from-youtube-dl", "fix music downloaded with youtube-dl", "usecase")
kw("fix-music-from-soulseek", "fix music from Soulseek downloads", "usecase")
kw("fix-music-from-bandcamp", "fix Bandcamp music tags", "usecase")
kw("fix-music-from-soundcloud", "fix SoundCloud music tags", "usecase")

# Technical how-to
kw("what-is-id3-tag", "what is an ID3 tag", "education")
kw("what-is-music-metadata", "what is music metadata", "education")
kw("what-is-album-art-mp3", "what is album art in MP3", "education")
kw("what-is-flac-tagging", "what is FLAC tagging", "education")
kw("what-is-acoustic-fingerprinting", "what is acoustic fingerprinting", "education")
kw("why-organize-music-library", "why organize your music library", "education")
kw("music-tag-types-explained", "music tag types explained", "education")
kw("id3v1-vs-id3v2-difference", "ID3v1 vs ID3v2 difference", "education")
kw("vorbis-comments-explained", "Vorbis comments explained", "education")
kw("flac-tags-vs-mp3-tags", "FLAC tags vs MP3 tags", "education")
kw("album-art-resolution-guide", "album art resolution guide", "education")
kw("embedded-vs-linked-album-art", "embedded vs linked album art", "education")
kw("music-library-structure-guide", "music library folder structure guide", "education")
kw("best-music-file-format-guide", "best music file format guide", "education")
kw("lossless-vs-lossy-music", "lossless vs lossy music explained", "education")
kw("mp3-bitrate-guide", "MP3 bitrate guide for music library", "education")
kw("flac-vs-mp3-quality", "FLAC vs MP3 quality comparison", "education")
kw("music-library-organization-tips", "music library organization tips 2025", "education")
kw("id3-tag-best-practices", "ID3 tag best practices", "education")
kw("music-metadata-standards", "music metadata standards guide", "education")

# Niche audience
kw("music-organizer-bedroom-producer", "music organizer bedroom producer", "niche")
kw("music-organizer-live-performer", "music organizer live performer", "niche")
kw("music-organizer-music-blogger", "music organizer music blogger", "niche")
kw("music-organizer-podcast-host", "music organizer podcast host", "niche")
kw("music-organizer-twitch-streamer", "music organizer Twitch streamer", "niche")
kw("music-organizer-youtube-creator", "music organizer YouTube creator", "niche")
kw("music-organizer-party-dj", "music organizer party DJ software", "niche")
kw("music-organizer-mobile-dj", "music organizer mobile DJ", "niche")
kw("music-organizer-club-dj", "music organizer club DJ software", "niche")
kw("music-organizer-wedding-dj", "music organizer wedding DJ", "niche")
kw("music-organizer-event-planner", "music organizer event planner", "niche")
kw("music-organizer-therapist", "music therapy library organizer", "niche")
kw("music-organizer-nursing-home", "music organizer nursing home activity", "niche")
kw("music-organizer-library-archivist", "music library archivist software", "niche")
kw("music-organizer-historian", "music historian collection organizer", "niche")

# Integrations
kw("music-organizer-plex-integration", "music organizer Plex integration", "integration")
kw("music-organizer-jellyfin-integration", "music organizer Jellyfin integration", "integration")
kw("music-organizer-kodi-integration", "music organizer Kodi integration", "integration")
kw("music-organizer-subsonic-integration", "music organizer Subsonic integration", "integration")
kw("music-organizer-airsonic-integration", "music organizer Airsonic integration", "integration")
kw("music-organizer-navidrome-integration", "music organizer Navidrome integration", "integration")
kw("music-organizer-synology-nas", "music organizer Synology NAS", "integration")
kw("music-organizer-qnap-nas", "music organizer QNAP NAS", "integration")
kw("music-organizer-dropbox", "music organizer Dropbox", "integration")
kw("music-organizer-google-drive", "music organizer Google Drive", "integration")
kw("music-organizer-onedrive", "music organizer OneDrive", "integration")
kw("music-organizer-icloud", "music organizer iCloud Music Library", "integration")

# Windows-specific extra
kw("windows-music-folder-organizer", "Windows music folder organizer", "platform")
kw("windows-media-player-fix", "fix Windows Media Player music tags", "platform")
kw("groove-music-tag-fix", "fix Groove Music tags Windows", "platform")
kw("windows-explorer-music-tags", "fix Windows Explorer music tags", "platform")
kw("file-explorer-music-info", "fix File Explorer music info Windows", "platform")
kw("windows-11-music-organizer", "best music organizer for Windows 11", "platform")
kw("windows-10-music-organizer-free", "free music organizer for Windows 10", "platform")
kw("64-bit-music-organizer", "64-bit music organizer Windows", "platform")
kw("music-organizer-no-install", "music organizer no install portable", "platform")
kw("portable-music-tagger", "portable music tagger Windows", "platform")

# macOS-specific extra
kw("mac-music-app-organizer", "Mac Music app organizer", "platform")
kw("mac-music-library-fixer", "Mac music library fixer", "platform")
kw("macos-music-tag-editor", "macOS music tag editor", "platform")
kw("mac-album-art-downloader", "Mac album art downloader", "platform")
kw("mac-id3-tag-fixer", "Mac ID3 tag fixer", "platform")
kw("mac-mp3-organizer", "Mac MP3 organizer software", "platform")
kw("mac-flac-organizer", "Mac FLAC organizer software", "platform")
kw("macos-music-library-manager", "macOS music library manager", "platform")
kw("apple-music-metadata-fixer", "Apple Music metadata fixer Mac", "platform")
kw("mac-duplicate-song-finder", "Mac duplicate song finder", "platform")

# Answer-the-public style questions
kw("can-i-fix-music-tags-for-free", "can I fix music tags for free", "questions")
kw("is-there-a-free-music-organizer", "is there a free music organizer", "questions")
kw("which-music-organizer-is-best", "which music organizer is best 2025", "questions")
kw("how-long-does-music-tagging-take", "how long does music library tagging take", "questions")
kw("does-tidymymusic-work-offline", "does TidyMyMusic work offline", "questions")
kw("will-music-organizer-delete-songs", "will music organizer delete my songs", "questions")
kw("can-music-tagger-find-rare-songs", "can music tagger find rare and obscure songs", "questions")
kw("how-accurate-is-acoustic-fingerprinting", "how accurate is acoustic fingerprinting", "questions")
kw("should-i-use-flac-or-mp3", "should I use FLAC or MP3 for my library", "questions")
kw("how-to-keep-music-library-organized", "how to keep music library organized long term", "questions")
kw("what-software-does-plex-use-for-music", "what software to use for Plex music metadata", "questions")
kw("best-software-for-10000-songs", "best software for organizing 10000 songs", "questions")
kw("can-music-organizer-fix-old-mp3s", "can music organizer fix old 90s MP3 downloads", "questions")
kw("does-music-organizer-work-with-iphone", "does music organizer work with iPhone sync", "questions")
kw("what-is-the-best-itunes-alternative", "what is the best iTunes music organizer alternative", "questions")

# Longtail extensions
kw("music-organizer-that-embeds-tags", "music organizer that embeds tags in files permanently", "longtail")
kw("music-tagger-reads-audio-not-filename", "music tagger that reads audio not just filename", "longtail")
kw("one-click-fix-music-library", "one click fix entire music library", "longtail")
kw("best-program-to-organize-mp3-files", "best program to organize MP3 files 2025", "longtail")
kw("software-to-fix-messy-itunes", "software to fix messy iTunes library", "longtail")
kw("best-software-to-tag-music-automatically", "best software to tag music automatically", "longtail")
kw("app-that-fixes-music-tags-automatically", "app that fixes music tags automatically", "longtail")
kw("program-to-download-missing-album-art", "program to download missing album artwork", "longtail")
kw("app-to-remove-duplicate-songs-itunes", "app to remove duplicate songs from iTunes", "longtail")
kw("software-to-find-song-names-automatically", "software to find song names automatically", "longtail")
kw("how-to-identify-songs-without-tags", "how to identify songs without any tags", "longtail")
kw("music-software-that-works-like-shazam", "music software that works like Shazam for desktop", "longtail")
kw("fix-music-library-for-home-theater", "fix music library for home theater system", "longtail")
kw("organize-music-for-network-attached-storage", "organize music for network attached storage", "longtail")
kw("tag-music-before-uploading-to-server", "tag music before uploading to media server", "longtail")
kw("best-music-organizer-for-large-flac-library", "best music organizer for large FLAC library", "longtail")
kw("how-to-fix-mislabeled-music-in-bulk", "how to fix mislabeled music in bulk", "longtail")
kw("music-library-organizer-no-internet-needed", "music library organizer no internet connection needed", "longtail")
kw("music-software-trusted-by-audiophiles", "music software trusted by audiophiles", "longtail")
kw("organize-music-by-decade-automatically", "organize music by decade automatically software", "longtail")

# ── Final push to 1000+ ───────────────────────
kw("music-organizer-2024", "music organizer software 2024", "organizer")
kw("music-organizer-free-2025", "free music organizer 2025", "organizer")
kw("download-music-manager", "download music manager software", "organizer")
kw("music-collection-tool", "music collection tool", "organizer")
kw("music-catalog-manager", "music catalog manager software", "organizer")
kw("music-inventory-software", "music inventory software", "organizer")
kw("digital-audio-organizer", "digital audio organizer", "organizer")
kw("digital-audio-management", "digital audio management software", "organizer")
kw("audio-collection-organizer", "audio collection organizer", "organizer")
kw("home-music-collection-software", "home music collection software", "organizer")
kw("music-lib-software", "music library software free download", "organizer")
kw("manage-digital-music", "manage digital music software", "organizer")
kw("music-curation-software", "music curation software", "organizer")
kw("music-archive-management", "music archive management software", "organizer")
kw("large-music-collection-software", "software for large music collection", "organizer")
kw("fix-music-tags-mac-free", "fix music tags Mac free", "tags")
kw("fix-music-tags-windows-free", "fix music tags Windows free software", "tags")
kw("tag-editor-mp3-free-download", "tag editor MP3 free download", "tags")
kw("mp3-tag-repair-software", "MP3 tag repair software", "tags")
kw("flac-tag-fixer-software", "FLAC tag fixer software", "tags")
kw("ogg-tag-editor-software", "OGG tag editor software", "tags")
kw("wav-tag-editor-software", "WAV tag editor software", "tags")
kw("wma-tag-editor-windows", "WMA tag editor Windows", "tags")
kw("aac-tag-editor-software", "AAC tag editor software", "tags")
kw("m4a-tag-fixer-software", "M4A tag fixer software", "tags")
kw("music-tag-writer-software", "music tag writer software", "tags")
kw("music-metadata-writer", "music metadata writer software", "tags")
kw("audio-metadata-editor", "audio metadata editor software", "tags")
kw("audio-metadata-fixer", "audio metadata fixer", "tags")
kw("id3-tag-software-free", "ID3 tag software free", "tags")
kw("id3-tag-editor-software-free", "ID3 tag editor software free download", "tags")
kw("music-tag-organizer", "music tag organizer software", "tags")
kw("music-tag-management", "music tag management software", "tags")
kw("automatic-cover-art-finder", "automatic cover art finder software", "artwork")
kw("album-cover-finder-software", "album cover finder software", "artwork")
kw("find-missing-album-covers", "find missing album covers software", "artwork")
kw("best-album-art-software", "best album art software 2025", "artwork")
kw("album-art-downloader-free", "free album art downloader software", "artwork")
kw("embed-artwork-automatically", "embed artwork automatically music", "artwork")
kw("album-thumbnail-fixer", "album thumbnail fixer software", "artwork")
kw("music-thumbnail-fix", "fix music thumbnail cover art", "artwork")
kw("itunes-artwork-fixer-tool", "iTunes artwork fixer tool", "artwork")
kw("itunes-cover-art-downloader", "iTunes cover art downloader software", "artwork")
kw("download-lyrics-automatically", "download song lyrics automatically software", "lyrics")
kw("lyrics-fetcher-software", "lyrics fetcher software", "lyrics")
kw("add-lyrics-automatically", "add lyrics to music automatically", "lyrics")
kw("music-lyrics-fixer", "music lyrics fixer software", "lyrics")
kw("embed-song-lyrics-software", "embed song lyrics software", "lyrics")
kw("itunes-lyrics-downloader", "iTunes lyrics downloader software", "lyrics")
kw("mp3-lyrics-embed-software", "MP3 lyrics embed software", "lyrics")
kw("best-lyrics-downloader", "best lyrics downloader software 2025", "lyrics")
kw("flac-lyrics-embed", "embed lyrics in FLAC files", "lyrics")
kw("music-duplicate-software", "music duplicate removal software", "duplicates")
kw("best-duplicate-remover-music", "best duplicate remover for music", "duplicates")
kw("music-duplicate-cleaner-free", "free music duplicate cleaner", "duplicates")
kw("delete-duplicate-mp3", "delete duplicate MP3 files software", "duplicates")
kw("duplicate-music-scanner", "duplicate music scanner software", "duplicates")
kw("duplicate-track-finder", "duplicate track finder software", "duplicates")
kw("remove-duplicate-flac", "remove duplicate FLAC files", "duplicates")
kw("duplicate-song-detector", "duplicate song detector software", "duplicates")
kw("music-duplicate-finder-windows", "music duplicate finder Windows", "duplicates")
kw("music-duplicate-finder-mac", "music duplicate finder Mac", "duplicates")
kw("iphone-music-sync-fix", "fix iPhone music sync issues", "device")
kw("ipad-music-sync-fix", "fix iPad music sync issues", "device")
kw("ipod-music-sync-fix", "fix iPod music sync issues", "device")
kw("music-sync-organized-iphone", "sync organized music to iPhone", "device")
kw("android-music-fix-tags", "fix music tags Android device", "device")
kw("car-stereo-music-tags", "fix music tags for car stereo", "device")
kw("usb-music-tags", "fix music tags for USB stick", "device")
kw("mp3-player-tags-fix", "fix MP3 player music tags", "device")
kw("sonos-music-organizer", "Sonos music library organizer", "device")
kw("denon-heos-music-organizer", "Denon HEOS music library organizer", "device")
kw("yamaha-musiccast-organizer", "Yamaha MusicCast library organizer", "device")
kw("music-server-metadata-fix", "fix music server metadata", "device")
kw("identify-song-from-audio", "identify song from audio file software", "tech")
kw("music-lookup-from-audio", "music lookup from audio file", "tech")
kw("song-finder-from-file", "song finder from audio file", "tech")
kw("music-recognition-pc", "music recognition software PC", "tech")
kw("music-id-software-windows", "music identification software Windows", "tech")
kw("fingerprint-audio-files", "fingerprint audio files software", "tech")
kw("acoustic-analysis-music", "acoustic analysis music software", "tech")
kw("music-identifier-software", "music identifier software desktop", "tech")
kw("offline-music-identifier", "offline music identifier software", "tech")
kw("music-recognizer-desktop", "music recognizer desktop app", "tech")
kw("best-music-library-app-pc", "best music library app for PC", "platform")
kw("best-music-manager-pc", "best music manager for PC 2025", "platform")
kw("best-music-manager-mac", "best music manager for Mac 2025", "platform")
kw("music-software-windows-11-free", "free music software Windows 11", "platform")
kw("music-library-app-free-mac", "free music library app Mac", "platform")
kw("music-app-windows-desktop", "music app Windows desktop organizer", "platform")
kw("music-file-app-mac", "music file organizer app Mac", "platform")
kw("light-music-organizer", "lightweight music organizer software", "platform")
kw("fast-music-organizer", "fast music organizer software", "platform")
kw("simple-music-organizer", "simple music organizer software", "platform")
kw("easy-music-organizer-software", "easy music organizer software", "platform")
kw("best-free-music-software", "best free music software 2025", "pricing")
kw("music-organizer-trial-version", "music organizer trial version download", "pricing")
kw("music-tagger-free-trial", "music tagger free trial", "pricing")
kw("best-music-software-value", "best value music software", "pricing")
kw("music-organizer-single-payment", "music organizer single payment", "pricing")
kw("music-tagger-no-monthly-fee", "music tagger no monthly fee", "pricing")
kw("affordable-itunes-cleaner", "affordable iTunes cleaner software", "pricing")
kw("cheap-mp3-tagger", "cheap MP3 tagger software", "pricing")
kw("music-organizer-coupon-2025", "music organizer coupon 2025", "pricing")
kw("tidymymusic-promo-code", "TidyMyMusic promo code", "pricing")
kw("organise-music-library-uk-software", "organise music library UK software", "global")
kw("music-organizer-deutsch", "Musik Bibliothek organisieren Software", "global")
kw("logiciel-organiser-musique", "logiciel organiser bibliothèque musique", "global")
kw("programa-organizar-musica", "programa para organizar música", "global")
kw("software-organizzare-musica", "software per organizzare musica", "global")
kw("music-library-software-nederland", "muziek bibliotheek software Nederland", "global")
kw("musika-organizer-polski", "organizator muzyki polskie oprogramowanie", "global")
kw("music-organizer-singapore", "music organizer software Singapore", "global")
kw("music-organizer-malaysia", "music organizer software Malaysia", "global")
kw("music-organizer-philippines", "music organizer software Philippines", "global")
kw("music-organizer-indonesia", "music organizer software Indonesia", "global")
kw("music-organizer-thailand", "music organizer software Thailand", "global")
kw("music-organizer-vietnam", "music organizer software Vietnam", "global")
kw("music-organizer-pakistan", "music organizer software Pakistan", "global")
kw("music-organizer-nigeria", "music organizer software Nigeria", "global")
kw("music-organizer-kenya", "music organizer software Kenya", "global")
kw("music-organizer-egypt", "music organizer software Egypt", "global")
kw("music-organizer-turkey", "music organizer software Turkey", "global")
kw("music-organizer-israel", "music organizer software Israel", "global")
kw("music-organizer-saudi-arabia", "music organizer software Saudi Arabia", "global")

print(f"Total keywords in database: {len(KEYWORDS)}")

# ─────────────────────────────────────────────
# 2. HTML TEMPLATE ENGINE
# ─────────────────────────────────────────────

COLORS = {
    "brand": ("#7c3aff", "#5b21b6"),
    "organizer": ("#0ea5e9", "#0369a1"),
    "itunes": ("#fc6d26", "#c05417"),
    "tags": ("#10b981", "#065f46"),
    "artwork": ("#f59e0b", "#92400e"),
    "lyrics": ("#ec4899", "#9d174d"),
    "duplicates": ("#ef4444", "#991b1b"),
    "tech": ("#6366f1", "#3730a3"),
    "format": ("#8b5cf6", "#5b21b6"),
    "platform": ("#14b8a6", "#0f766e"),
    "device": ("#f97316", "#c2410c"),
    "howto": ("#22c55e", "#15803d"),
    "audience": ("#a855f7", "#7e22ce"),
    "genre": ("#e879f9", "#a21caf"),
    "compare": ("#64748b", "#334155"),
    "global": ("#06b6d4", "#0e7490"),
    "batch": ("#84cc16", "#3f6212"),
    "storage": ("#f43f5e", "#9f1239"),
    "sorting": ("#0891b2", "#155e75"),
    "ripping": ("#d97706", "#78350f"),
    "migration": ("#7c3aed", "#4c1d95"),
    "pricing": ("#16a34a", "#14532d"),
    "pro": ("#1d4ed8", "#1e3a8a"),
    "longtail": ("#7c3aff", "#4c1d95"),
}

def accent(cat):
    return COLORS.get(cat, ("#7c3aff", "#5b21b6"))

BASE_CSS = """
<style>
  :root{--ink:#0e0e10;--paper:#f7f5f0;--card:#fff;--border:#e2e0db;--muted:#6b6b70;--groove:#1a1a2e}
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
  html{scroll-behavior:smooth}
  body{background:var(--paper);color:var(--ink);font-family:'Segoe UI',system-ui,sans-serif;font-size:16px;line-height:1.65;overflow-x:hidden}
  a{color:#7c3aff;text-decoration:none}
  a:hover{text-decoration:underline}
  nav{position:sticky;top:0;z-index:100;background:var(--groove);display:flex;align-items:center;justify-content:space-between;padding:0 2rem;height:56px}
  .nl{font-size:1.2rem;color:#fff;font-weight:700;letter-spacing:-.02em}
  .nl span{color:#00d4aa}
  .nlinks{display:flex;gap:1.5rem;align-items:center}
  .nlinks a{color:rgba(255,255,255,.7);font-size:.85rem;font-weight:500}
  .nlinks a:hover{color:#fff;text-decoration:none}
  .ncta{background:#7c3aff;color:#fff!important;padding:.35rem 1rem;border-radius:6px;font-weight:700}
  .hero{background:var(--groove);color:#fff;padding:5rem 2rem 4rem;text-align:center;position:relative;overflow:hidden}
  .hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 70% 50% at 50% 110%,var(--ha) 0%,transparent 70%);pointer-events:none}
  .eyebrow{display:inline-block;border-radius:100px;font-size:.75rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:.25rem .9rem;margin-bottom:1.25rem;border:1px solid var(--hb);color:var(--hb);background:rgba(255,255,255,.08)}
  h1{font-size:clamp(2rem,5vw,3.5rem);line-height:1.1;letter-spacing:-.03em;max-width:820px;margin:0 auto 1.2rem}
  h1 em{color:#00d4aa;font-style:italic}
  .hsub{font-size:1.05rem;color:rgba(255,255,255,.7);max-width:580px;margin:0 auto 2.2rem}
  .btn-p{background:var(--ha);color:#fff;padding:.85rem 2rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
  .btn-p:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,0,0,.3);text-decoration:none}
  section{padding:5rem 2rem}
  .container{max-width:1080px;margin:0 auto}
  .sec-ey{font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ha);margin-bottom:.6rem}
  h2{font-size:clamp(1.8rem,3.5vw,2.6rem);line-height:1.1;letter-spacing:-.02em;margin-bottom:.8rem}
  .sec-sub{color:var(--muted);max-width:580px;font-size:1rem;margin-bottom:3rem}
  .grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem}
  .grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.5rem}
  .card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem;transition:box-shadow .2s,transform .2s}
  .card:hover{box-shadow:0 10px 36px rgba(0,0,0,.07);transform:translateY(-2px)}
  .fi{width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:1rem;background:var(--fa)}
  .card h3{font-size:1rem;font-weight:700;margin-bottom:.4rem}
  .card p,.card li{font-size:.88rem;color:var(--muted)}
  .card ul{padding-left:1.1rem;margin-top:.4rem}
  .card ul li{margin-bottom:.2rem}
  .kw-cloud{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1.5rem}
  .kw{background:var(--card);border:1px solid var(--border);border-radius:6px;padding:.25rem .7rem;font-size:.78rem;color:var(--muted)}
  .steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:2rem;margin-top:2.5rem}
  .step{text-align:center}
  .sn{display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:50%;background:var(--ha);color:#fff;font-size:1.3rem;font-weight:700;margin-bottom:.9rem}
  .step h3{font-size:.95rem;font-weight:700;margin-bottom:.3rem}
  .step p{font-size:.83rem;color:var(--muted)}
  .cta-strip{background:linear-gradient(135deg,var(--ha) 0%,var(--hb) 100%);color:#fff;text-align:center;padding:5rem 2rem}
  .cta-strip h2{color:#fff;margin-bottom:.9rem}
  .cta-strip p{color:rgba(255,255,255,.8);max-width:480px;margin:0 auto 2rem;font-size:1rem}
  .btn-w{background:#fff;color:var(--ha);padding:.9rem 2.2rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
  .btn-w:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.2);text-decoration:none}
  .bcrumb{font-size:.8rem;color:var(--muted);padding:1rem 2rem;max-width:1080px;margin:0 auto}
  .bcrumb a{color:var(--muted)}
  footer{background:var(--ink);color:rgba(255,255,255,.55);padding:3rem 2rem 2rem;font-size:.82rem}
  .fg{max-width:1080px;margin:0 auto;display:flex;flex-wrap:wrap;gap:2rem;justify-content:space-between;margin-bottom:2rem}
  .fc h4{color:#fff;font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.75rem}
  .fc ul{list-style:none}
  .fc ul li{margin-bottom:.35rem}
  .fc ul li a{color:rgba(255,255,255,.5);font-size:.82rem}
  .fc ul li a:hover{color:#fff;text-decoration:none}
  .fb{max-width:1080px;margin:.2rem auto 0;border-top:1px solid rgba(255,255,255,.1);padding-top:1.5rem;display:flex;justify-content:space-between;flex-wrap:wrap;gap:.5rem;font-size:.76rem}
  .aff{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:5px;padding:.4rem .9rem;font-size:.76rem;margin-top:1rem;max-width:580px}
  @media(max-width:640px){.nlinks a:not(.ncta){display:none}.hero{padding:3.5rem 1.25rem 3rem}h1{font-size:2rem}.steps{grid-template-columns:1fr 1fr}}
</style>
"""

def nav_html():
    return f"""
<nav>
  <a class="nl" href="{BASE_PATH}/">Tidy<span>My</span>Music</a>
  <div class="nlinks">
    <a href="{BASE_PATH}/">Home</a>
    <a href="{BASE_PATH}/features.html">Features</a>
    <a href="{BASE_PATH}/how-it-works.html">How It Works</a>
    <a href="{BASE_PATH}/compare.html">Compare</a>
    <a href="{BASE_PATH}/faq.html">FAQ</a>
    <a href="{AFFILIATE_URL}" class="ncta" target="_blank" rel="nofollow sponsored">⬇ Download Free</a>
  </div>
</nav>"""

def footer_html():
    return f"""
<footer>
  <div class="fg">
    <div class="fc">
      <h4>TidyMyMusic</h4>
      <p style="max-width:220px;color:rgba(255,255,255,.5);font-size:.82rem;margin-bottom:.75rem">The world's most trusted music library organizer — fix tags, art & duplicates automatically.</p>
      <div class="aff">🔗 Affiliate site. We earn a commission at no extra cost to you.</div>
    </div>
    <div class="fc">
      <h4>Features</h4>
      <ul>
        <li><a href="{BASE_PATH}/id3-tag-fixer.html">ID3 Tag Fixer</a></li>
        <li><a href="{BASE_PATH}/album-art-downloader.html">Album Art</a></li>
        <li><a href="{BASE_PATH}/duplicate-song-remover.html">Duplicate Remover</a></li>
        <li><a href="{BASE_PATH}/lyrics-downloader-mp3.html">Lyrics Download</a></li>
        <li><a href="{BASE_PATH}/batch-mp3-tagger.html">Batch Processing</a></li>
        <li><a href="{BASE_PATH}/acoustic-fingerprint-music.html">Fingerprinting</a></li>
      </ul>
    </div>
    <div class="fc">
      <h4>Platforms</h4>
      <ul>
        <li><a href="{BASE_PATH}/music-organizer-windows-10.html">Windows 10</a></li>
        <li><a href="{BASE_PATH}/music-organizer-windows-11.html">Windows 11</a></li>
        <li><a href="{BASE_PATH}/music-organizer-macos.html">macOS</a></li>
        <li><a href="{BASE_PATH}/itunes-library-organizer.html">iTunes</a></li>
        <li><a href="{BASE_PATH}/iphone-music-organizer.html">iPhone</a></li>
      </ul>
    </div>
    <div class="fc">
      <h4>Compare</h4>
      <ul>
        <li><a href="{BASE_PATH}/vs-mp3tag.html">vs Mp3tag</a></li>
        <li><a href="{BASE_PATH}/vs-musicbrainz-picard.html">vs MusicBrainz</a></li>
        <li><a href="{BASE_PATH}/vs-mediamonkey.html">vs MediaMonkey</a></li>
        <li><a href="{BASE_PATH}/best-music-organizer-2025.html">Best 2025</a></li>
        <li><a href="{BASE_PATH}/compare.html">Full Comparison</a></li>
      </ul>
    </div>
    <div class="fc">
      <h4>Resources</h4>
      <ul>
        <li><a href="{BASE_PATH}/faq.html">FAQ</a></li>
        <li><a href="{BASE_PATH}/blog.html">Blog</a></li>
        <li><a href="{BASE_PATH}/sitemap.xml">Sitemap</a></li>
        <li><a href="{BASE_PATH}/llms.txt">llms.txt</a></li>
        <li><a href="{AFFILIATE_URL}" rel="nofollow sponsored">Download</a></li>
      </ul>
    </div>
  </div>
  <div class="fb">
    <span>© {date.today().year} TidyMyMusic Affiliate Site. TidyMyMusic is a product of Wondershare Software Co., Ltd.</span>
    <span>Available Worldwide · Windows &amp; macOS</span>
  </div>
</footer>"""

def schema_software():
    return f"""
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"TidyMyMusic","operatingSystem":"Windows, macOS","applicationCategory":"MultimediaApplication","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial available"}},"description":"TidyMyMusic automatically fixes ID3 tags, downloads album artwork, retrieves lyrics, and removes duplicate songs using acoustic fingerprinting.","url":"{AFFILIATE_URL}","publisher":{{"@type":"Organization","name":"Wondershare Software"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.5","reviewCount":"2847","bestRating":"5"}}}}
</script>"""

def build_keyword_page(kw_data, related=None):
    """Generate a full SEO-optimized HTML page for a keyword."""
    slug = kw_data["slug"]
    keyword = kw_data["keyword"]
    cat = kw_data["cat"]
    ac, ac2 = accent(cat)
    related = related or []

    title = f"{keyword} — TidyMyMusic"
    desc  = f"Looking for the best {keyword.lower()} solution? TidyMyMusic automatically fixes music tags, downloads album art, removes duplicates and cleans your library in one click. Free trial available."

    features = [
        ("🔊", "Acoustic Fingerprint ID", "Identifies songs even with completely blank tags using audio analysis."),
        ("🏷️", "Auto ID3 Tag Repair", "Fix artist, album, title, year, genre & track numbers in batch."),
        ("🖼️", "Album Art Download", "Fetch and embed high-res artwork for every track automatically."),
        ("📝", "Lyrics Embed", "Download and embed synchronized or static lyrics into audio files."),
        ("🗑️", "Duplicate Removal", "Find and delete duplicate tracks by metadata and audio similarity."),
        ("⚡", "Batch Processing", "Process thousands of songs in one click — no manual work needed."),
    ]

    related_links = ""
    if related:
        related_links = "<div class='kw-cloud'>" + "".join(
            "<a class='kw' href='" + BASE_PATH + "/{}.html'>{}</a>".format(r["slug"], r["keyword"]) for r in related[:18]
        ) + "</div>"

    feature_cards = "".join(f"""
      <div class="card" style="--fa:rgba(124,58,255,.1)">
        <div class="fi">{icon}</div>
        <h3>{name}</h3>
        <p>{desc_}</p>
      </div>""" for icon, name, desc_ in features)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{title}</title>
  <meta name="description" content="{desc}"/>
  <meta name="keywords" content="{keyword}, TidyMyMusic, music library organizer, ID3 tag fixer, album art downloader, duplicate song remover, music metadata editor, MP3 tag editor, iTunes cleaner, acoustic fingerprinting, batch music tagger"/>
  <link rel="canonical" href="{SITE_DOMAIN}/{slug}.html"/>
  <meta property="og:title" content="{title}"/>
  <meta property="og:description" content="{desc}"/>
  <meta property="og:type" content="website"/>
  <meta name="robots" content="index,follow"/>
  <style>:root{{--ha:{ac};--hb:{ac2}}}</style>
  {BASE_CSS}
  {schema_software()}
</head>
<body>
{nav_html()}

<div class="bcrumb container">
  <a href="{BASE_PATH}/">Home</a> &rsaquo; <a href="{BASE_PATH}/keywords.html">All Topics</a> &rsaquo; {keyword}
</div>

<section class="hero">
  <div class="eyebrow">✦ {cat.title()} Solution</div>
  <h1>The Best <em>{keyword}</em><br>Software in 2025</h1>
  <p class="hsub">TidyMyMusic is the world's most trusted {keyword.lower()} tool — fix tags, download artwork, remove duplicates and organise your entire collection automatically.</p>
  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">🎵 Download Free Trial</a>
</section>

<section style="background:#fff">
  <div class="container">
    <div class="sec-ey">Why TidyMyMusic for {keyword}</div>
    <h2>Everything You Need in One Tool</h2>
    <p class="sec-sub">Whether you need {keyword.lower()} for a small playlist or a 50,000-song library, TidyMyMusic handles it automatically — no technical skills required.</p>
    <div class="grid2">{feature_cards}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-ey">How It Works</div>
    <h2>From Messy to Perfect in 3 Steps</h2>
    <p class="sec-sub">The simplest {keyword.lower()} workflow you've ever used.</p>
    <div class="steps">
      <div class="step">
        <div class="sn">1</div>
        <h3>Import Library</h3>
        <p>Connect your iTunes library or point to any local music folder. Supports libraries of any size.</p>
      </div>
      <div class="step">
        <div class="sn">2</div>
        <h3>Click Identify</h3>
        <p>Acoustic fingerprinting and online music databases identify every track and suggest correct metadata.</p>
      </div>
      <div class="step">
        <div class="sn">3</div>
        <h3>Save &amp; Sync</h3>
        <p>Tags are embedded into the audio file itself — sync to iPhone, iPad, or any device instantly.</p>
      </div>
    </div>
  </div>
</section>

<section style="background:#fff">
  <div class="container">
    <div class="sec-ey">About TidyMyMusic</div>
    <h2>{keyword} — Full Overview</h2>
    <div style="max-width:780px;color:var(--muted);font-size:.95rem;line-height:1.8">
      <p style="margin-bottom:1rem">TidyMyMusic by Wondershare is a leading {keyword.lower()} application trusted by millions of music fans worldwide. It uses advanced acoustic fingerprint technology to identify songs even when metadata is completely missing — then automatically downloads the correct artist name, album title, track number, year, genre, album artwork, and lyrics.</p>
      <p style="margin-bottom:1rem">The software supports batch processing, meaning you can fix an entire library of 10,000+ songs in a single session. All tag updates are embedded directly into the audio file (MP3, FLAC, M4A, WAV, and more), so your organised library travels with you to any device — iPhone, iPad, Android, car stereo, home media server, or NAS.</p>
      <p>For anyone searching for a reliable {keyword.lower()} solution, TidyMyMusic offers the most complete feature set available: tag repair, artwork recovery, lyrics embedding, duplicate detection, and iTunes integration — all in one intuitive application.</p>
    </div>
    <div style="margin-top:2rem">
      <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">⬇ Download Free Trial — No Credit Card Required</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-ey">Related Topics</div>
    <h2>Explore More Music Organisation Topics</h2>
    {related_links}
  </div>
</section>

<div class="cta-strip">
  <h2>Start Organising Your Music Today</h2>
  <p>Join millions of music lovers worldwide. Download TidyMyMusic free and see the difference in minutes.</p>
  <a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">🎶 Download TidyMyMusic Free</a>
</div>

{footer_html()}
</body>
</html>"""

# ─────────────────────────────────────────────
# 3. ESSENTIAL SITE PAGES
# ─────────────────────────────────────────────

def page_index():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>TidyMyMusic — #1 Music Library Organizer | Fix Tags, Art &amp; Duplicates Automatically</title>
  <meta name="description" content="TidyMyMusic automatically fixes ID3 tags, downloads album artwork, removes duplicate songs, and organizes your iTunes or local music library in one click. Free trial — Windows &amp; Mac."/>
  <meta name="keywords" content="music library organizer, iTunes cleaner, ID3 tag fixer, album art downloader, duplicate song remover, music metadata editor, MP3 tag editor, batch music tagger, acoustic fingerprint, TidyMyMusic, Wondershare TidyMyMusic"/>
  <link rel="canonical" href="{SITE_DOMAIN}/"/>
  <meta property="og:title" content="TidyMyMusic — #1 Music Library Organizer"/>
  <meta property="og:description" content="Fix tags, download artwork, remove duplicates and clean your entire music collection in one click."/>
  <meta property="og:type" content="website"/>
  <meta name="robots" content="index,follow"/>
  <style>:root{{--ha:#7c3aff;--hb:#5b21b6;--fa:rgba(124,58,255,.1)}}</style>
  {BASE_CSS}
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"WebSite","name":"TidyMyMusic","url":"{SITE_DOMAIN}","description":"Music library organizer that fixes tags, artwork, lyrics and removes duplicate songs automatically."}}
  </script>
  {schema_software()}
</head>
<body>
{nav_html()}
<section class="hero">
  <div class="eyebrow">✦ The World's Favourite Music Library Organizer</div>
  <h1>Your Music Library,<br><em>Finally Tidy.</em></h1>
  <p class="hsub">Fix missing tags, download album artwork, remove duplicates and organise thousands of songs automatically — in a single click.</p>
  <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
    <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">🎵 Download Free Trial</a>
    <a href="{BASE_PATH}/how-it-works.html" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:rgba(255,255,255,.85);padding:.85rem 2rem;border-radius:8px;font-weight:600;font-size:1rem;display:inline-block">See How It Works</a>
  </div>
  <div style="display:flex;justify-content:center;gap:3rem;margin-top:3.5rem;padding-top:3rem;border-top:1px solid rgba(255,255,255,.1);flex-wrap:wrap">
    <div style="text-align:center"><span style="font-size:2.2rem;color:#fff;display:block;font-weight:800">5M+</span><span style="font-size:.75rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.06em">Music Fans</span></div>
    <div style="text-align:center"><span style="font-size:2.2rem;color:#fff;display:block;font-weight:800">1-Click</span><span style="font-size:.75rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.06em">Full Library Cleanup</span></div>
    <div style="text-align:center"><span style="font-size:2.2rem;color:#fff;display:block;font-weight:800">99%</span><span style="font-size:.75rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.06em">Tag Accuracy</span></div>
    <div style="text-align:center"><span style="font-size:2.2rem;color:#fff;display:block;font-weight:800">10+</span><span style="font-size:.75rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.06em">Audio Formats</span></div>
  </div>
</section>

<section style="background:#fff8f6;border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:3rem 2rem">
  <div class="container">
    <div class="grid3">
      <div class="card"><div class="fi">😤</div><h3>"Unknown Artist – Track 01"</h3><p>Hundreds of songs with no name, no album, no way to find what you want.</p></div>
      <div class="card"><div class="fi">🖼️</div><h3>Missing Album Artwork</h3><p>Grey boxes everywhere. Your music player looks empty without cover art.</p></div>
      <div class="card"><div class="fi">📀</div><h3>Duplicates Eating Your Storage</h3><p>The same track ripped twice, downloaded three times — wasting gigabytes.</p></div>
      <div class="card"><div class="fi">🔀</div><h3>Mislabelled &amp; Wrong Info</h3><p>Wrong artist names, wrong years, mixed-up genres — a complete mess.</p></div>
      <div class="card"><div class="fi">⏱️</div><h3>Manual Editing Takes Forever</h3><p>Fixing 8,000 songs one by one is not a weekend project. It's a lifetime project.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-ey">All Features</div>
    <h2>Everything Your Music Library Needs</h2>
    <p class="sec-sub">TidyMyMusic packs every music organisation tool into one intuitive app.</p>
    <div class="grid2">
      <div class="card"><div class="fi">🔊</div><h3>Acoustic Fingerprint ID</h3><p>Even with completely blank tags, TidyMyMusic listens to the audio and matches it to the correct song in global music databases.</p></div>
      <div class="card"><div class="fi">🏷️</div><h3>Auto ID3 Tag Repair</h3><p>Fix missing or wrong artist, album, title, track number, year, genre and composer tags in bulk — embedded directly into the file.</p></div>
      <div class="card"><div class="fi">🖼️</div><h3>Album Art Recovery</h3><p>Automatically download high-resolution album cover art for every track. Transform grey boxes into a beautiful visual library.</p></div>
      <div class="card"><div class="fi">📝</div><h3>Lyrics Embed</h3><p>Find and embed lyrics for every song automatically. Follow along or simply enjoy a fully-enriched music library.</p></div>
      <div class="card"><div class="fi">🗑️</div><h3>Smart Duplicate Detection</h3><p>Scan by metadata and audio similarity, review matches, and remove unnecessary copies to free gigabytes of storage.</p></div>
      <div class="card"><div class="fi">⚡</div><h3>One-Click Batch Processing</h3><p>Import your entire library and hit Identify. Thousands of songs processed in minutes — not months.</p></div>
    </div>
    <div style="margin-top:2.5rem;text-align:center">
      <a href="{BASE_PATH}/features.html" style="color:var(--ha);font-weight:600;font-size:.95rem">View all features →</a>
    </div>
  </div>
</section>

<section style="background:#1a1a2e;color:#fff">
  <div class="container">
    <div class="sec-ey" style="color:#00d4aa">Supported Formats</div>
    <h2 style="color:#fff">Works With Every Format You Own</h2>
    <div class="kw-cloud" style="margin-top:1.5rem">
      {''.join(f'<span class="kw" style="background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.15);color:rgba(255,255,255,.7)">{f}</span>' for f in ["MP3","FLAC","M4A","AAC","WAV","WMA","OGG","AIFF","APE","MP4 Audio","iTunes Library","Local Folders","Windows 10","Windows 11","macOS Sequoia","macOS Sonoma","macOS Ventura"])}
    </div>
  </div>
</section>

<section style="background:#f0edff">
  <div class="container">
    <div class="sec-ey">Real Users</div>
    <h2>Music Fans Around the World Love TidyMyMusic</h2>
    <div class="grid2">
      <div class="card"><div style="color:#f59e0b;margin-bottom:.75rem">★★★★★</div><p style="color:var(--ink);margin-bottom:1.2rem">"I have over 15,000 songs — TidyMyMusic found 99% of missing artwork and tags in one afternoon. Absolutely amazing."</p><strong style="font-size:.85rem">David R. — London, UK 🇬🇧</strong></div>
      <div class="card"><div style="color:#f59e0b;margin-bottom:.75rem">★★★★★</div><p style="color:var(--ink);margin-bottom:1.2rem">"As a DJ with 20,000 tracks, correct genre tags are critical. TidyMyMusic fixed my entire library accurately. The fingerprinting is genuinely impressive."</p><strong style="font-size:.85rem">Kenji W. — Tokyo, Japan 🇯🇵</strong></div>
      <div class="card"><div style="color:#f59e0b;margin-bottom:.75rem">★★★★☆</div><p style="color:var(--ink);margin-bottom:1.2rem">"TidyMyMusic cleaned 15,000 songs and found almost everything. So intuitive — even my wife uses it now!"</p><strong style="font-size:.85rem">James T. — Sydney, Australia 🇦🇺</strong></div>
      <div class="card"><div style="color:#f59e0b;margin-bottom:.75rem">★★★★★</div><p style="color:var(--ink);margin-bottom:1.2rem">"Tenía más de 10,000 canciones sin portadas. TidyMyMusic lo arregló todo automáticamente. ¡Completamente recomendado!"</p><strong style="font-size:.85rem">Carlos M. — Madrid, España 🇪🇸</strong></div>
    </div>
  </div>
</section>

<div class="cta-strip">
  <h2>Your Perfect Music Library Is One Click Away</h2>
  <p>Join millions of music fans worldwide. Download TidyMyMusic free and see the difference in minutes.</p>
  <a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">🎶 Download TidyMyMusic Free</a>
</div>
{footer_html()}
</body>
</html>"""


def page_features():
    features = [
        ("🔊","Acoustic Fingerprint Identification","Even with completely blank tags, TidyMyMusic analyses the actual audio to match songs in global databases — no title, no problem."),
        ("🏷️","ID3 Tag Auto-Repair","Fix artist, album, title, track number, year, genre, composer and more. Tags are embedded directly in the file for cross-device portability."),
        ("🖼️","Album Artwork Recovery","Fetch and embed high-resolution cover art for every song. Transforms your music player from a grey grid into a beautiful visual collection."),
        ("📝","Lyrics Download & Embed","Find and embed synchronized or static lyrics automatically. Follow along or archive — your choice."),
        ("🗑️","Smart Duplicate Detection","Scan by metadata AND audio similarity. Review potential duplicates and remove copies to reclaim gigabytes of storage."),
        ("⚡","Batch Processing","Process thousands of songs in one click. What would take months manually is done in minutes."),
        ("🎵","iTunes Integration","Seamless two-way sync with iTunes on Mac and Windows. Changes reflect automatically — syncs to iPhone, iPad, iPod."),
        ("📁","Local Folder Support","Not an iTunes user? Point TidyMyMusic at any folder on your PC or Mac — it works the same."),
        ("✏️","Manual Tag Override","Review all suggestions and override any field. Drag-and-drop artwork, type custom tags, full control."),
        ("💾","Embedded Tags Stay Forever","Tags live inside the audio file — copy to USB, sync to phone, upload to NAS — metadata always travels with the music."),
        ("🔄","Multi-Format Support","MP3, FLAC, M4A, AAC, WAV, WMA, OGG, AIFF, APE and more. The most comprehensive format support available."),
        ("🌍","Global Music Database","Connected to worldwide music databases to identify tracks from every genre, country and era."),
    ]
    cards = "".join(f'<div class="card"><div class="fi">{i}</div><h3>{n}</h3><p>{d}</p></div>' for i,n,d in features)
    return f"""<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>TidyMyMusic Features — ID3 Tags, Album Art, Duplicates, Lyrics & More</title>
  <meta name="description" content="Full feature list for TidyMyMusic: acoustic fingerprinting, ID3 tag repair, album art download, lyrics embed, duplicate removal, iTunes integration and batch processing."/>
  <link rel="canonical" href="{SITE_DOMAIN}/features.html"/>
  <style>:root{{--ha:#7c3aff;--hb:#5b21b6;--fa:rgba(124,58,255,.1)}}</style>
  {BASE_CSS}
</head><body>
{nav_html()}
<section class="hero"><div class="eyebrow">✦ Complete Feature List</div>
  <h1>Everything TidyMyMusic<br><em>Can Do For You</em></h1>
  <p class="hsub">One tool. Every music organisation task covered. Free trial available right now.</p>
  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">⬇ Download Free Trial</a>
</section>
<section style="background:#fff"><div class="container">
  <div class="sec-ey">All Features</div><h2>12 Powerful Music Organizer Features</h2>
  <p class="sec-sub">TidyMyMusic covers every aspect of music library management in a single application.</p>
  <div class="grid2">{cards}</div>
</div></section>
<div class="cta-strip"><h2>Try All Features Free</h2><p>Download the free trial and experience TidyMyMusic's full feature set today.</p>
  <a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">🎶 Download TidyMyMusic Free</a>
</div>
{footer_html()}</body></html>"""


def page_how_it_works():
    return f"""<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>How TidyMyMusic Works — 4 Simple Steps to a Perfect Music Library</title>
  <meta name="description" content="Learn how TidyMyMusic organizes your music library in 4 steps: import, identify, review, and save. Acoustic fingerprinting does the hard work for you."/>
  <link rel="canonical" href="{SITE_DOMAIN}/how-it-works.html"/>
  <style>:root{{--ha:#7c3aff;--hb:#5b21b6;--fa:rgba(124,58,255,.1)}}</style>
  {BASE_CSS}
</head><body>
{nav_html()}
<section class="hero"><div class="eyebrow">✦ Step-by-Step Guide</div>
  <h1>From Chaos to<br><em>Perfect Library</em></h1>
  <p class="hsub">TidyMyMusic organises your entire music collection in 4 simple steps. No technical knowledge required.</p>
  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">⬇ Download Free Trial</a>
</section>
<section><div class="container">
  <div class="sec-ey">The Process</div><h2>4 Steps to a Perfect Music Library</h2>
  <div class="steps">
    <div class="step"><div class="sn">1</div><h3>Import Your Library</h3><p>Connect your iTunes library or point TidyMyMusic at any local music folder on your PC or Mac. Supports libraries of any size — even 50,000+ songs.</p></div>
    <div class="step"><div class="sn">2</div><h3>Click Identify</h3><p>Hit the Identify button. Acoustic fingerprinting and global music databases identify every song and suggest the correct artist, album, title, year, genre and artwork.</p></div>
    <div class="step"><div class="sn">3</div><h3>Review Suggestions</h3><p>Browse all suggestions before saving. Override any field manually, drag-and-drop custom artwork, or accept everything with one click.</p></div>
    <div class="step"><div class="sn">4</div><h3>Save &amp; Enjoy</h3><p>Tags are embedded into the audio file itself. Sync to your iPhone, iPad, NAS, or any device. Your beautiful library goes everywhere you go.</p></div>
  </div>
</div></section>
<section style="background:#fff"><div class="container">
  <div class="sec-ey">Technology</div><h2>How Acoustic Fingerprinting Works</h2>
  <div style="max-width:720px;color:var(--muted);font-size:.95rem;line-height:1.8">
    <p style="margin-bottom:1rem">Acoustic fingerprinting analyses the actual audio content of your music file — independent of any existing (or missing) tags. The audio waveform is converted into a unique digital fingerprint and compared against a global database of millions of songs.</p>
    <p style="margin-bottom:1rem">This means TidyMyMusic can correctly identify a song even if it's named "track01.mp3" with no other information at all. The fingerprint is tied to the music itself, not the filename or existing tags.</p>
    <p>Once identified, TidyMyMusic retrieves all available metadata from the database and allows you to embed it directly into the audio file — ensuring the correct information travels with your music wherever it goes.</p>
  </div>
</div></section>
<div class="cta-strip"><h2>See It In Action — Free Trial</h2><p>Download TidyMyMusic and run it on your own library right now. No credit card required.</p>
  <a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">🎶 Download TidyMyMusic Free</a>
</div>
{footer_html()}</body></html>"""


def page_faq():
    faqs = [
        ("What is TidyMyMusic?", "TidyMyMusic is a music library organiser by Wondershare that automatically fixes ID3 tags, downloads album artwork, retrieves lyrics, and removes duplicate songs from iTunes or local music folders using acoustic fingerprinting."),
        ("Does TidyMyMusic work with iTunes?", "Yes. TidyMyMusic integrates seamlessly with iTunes on both Windows and Mac. Changes reflect automatically in your library and sync to iPhone, iPad, or iPod."),
        ("What audio formats are supported?", "MP3, M4A, AAC, FLAC, WAV, WMA, OGG, AIFF, APE and other common formats. Works with iTunes libraries and local folders."),
        ("How does acoustic fingerprinting work?", "It analyses the actual audio content — independent of tags — to create a unique fingerprint matched against global music databases. Works even on completely untagged files."),
        ("Is TidyMyMusic safe for my library?", "Yes. You review all suggested changes before saving. Audio content is never modified — only metadata tags. Your original music is always preserved."),
        ("How many songs can it handle?", "Users regularly run it on 10,000–50,000+ song collections. Batch processing handles multiple files simultaneously."),
        ("Is there a free trial?", "Yes. Download the free trial and try TidyMyMusic on your own library before purchasing. No credit card required."),
        ("Does it work on Mac and Windows?", "Yes — available for Windows 7/8/10/11 and all major macOS versions including Sequoia, Sonoma, Ventura and Monterey."),
        ("Will fixed tags stay when I copy music?", "Yes. Tags are embedded into the audio file itself, so they travel with the music to any device — phone, tablet, car stereo, NAS, or media server."),
        ("Can it find art for obscure albums?", "TidyMyMusic searches multiple databases. Mainstream releases are found almost every time. For very obscure releases you can manually drag-and-drop artwork."),
        ("How does duplicate detection work?", "Scans by both metadata (artist, title, duration) and audio similarity, then presents potential duplicates for review so you decide what to keep."),
        ("What is an ID3 tag?", "ID3 tags are metadata stored inside audio files containing artist, album, title, track number, genre, year, artwork and lyrics. TidyMyMusic fixes and fills all of these automatically."),
        ("Does it support FLAC files?", "Yes. TidyMyMusic fully supports FLAC and other lossless formats — perfect for audiophile collections."),
        ("Can I edit tags manually?", "Yes. Manually override any auto-suggested tag, drag-and-drop artwork, or type custom information at any point."),
        ("Is it good for large libraries?", "Absolutely. TidyMyMusic is specifically designed for large collections. Batch processing means a 10,000-song library that would take months manually can be cleaned up in an afternoon."),
    ]
    items = "".join(f'<div class="card" style="--fa:rgba(124,58,255,.1)"><h3>{q}</h3><p style="margin-top:.5rem">{a}</p></div>' for q,a in faqs)
    faq_schema = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}, indent=2)
    return f"""<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>TidyMyMusic FAQ — Frequently Asked Questions</title>
  <meta name="description" content="Answers to the most common TidyMyMusic questions: features, compatibility, acoustic fingerprinting, ID3 tags, duplicates, pricing and more."/>
  <link rel="canonical" href="{SITE_DOMAIN}/faq.html"/>
  <style>:root{{--ha:#7c3aff;--hb:#5b21b6;--fa:rgba(124,58,255,.1)}}</style>
  {BASE_CSS}
  <script type="application/ld+json">{faq_schema}</script>
</head><body>
{nav_html()}
<section class="hero"><div class="eyebrow">✦ Frequently Asked Questions</div>
  <h1>Everything You Need to<br><em>Know About TidyMyMusic</em></h1>
  <p class="hsub">Answers to the most common questions about TidyMyMusic features, compatibility, and how it works.</p>
</section>
<section><div class="container">
  <div class="sec-ey">FAQ</div><h2>15 Common Questions Answered</h2>
  <div class="grid2">{items}</div>
</div></section>
<div class="cta-strip"><h2>Ready to Try TidyMyMusic?</h2><p>Download the free trial and organise your music library in minutes.</p>
  <a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">🎶 Download Free Trial</a>
</div>
{footer_html()}</body></html>"""


def page_compare():
    rows = [
        ("Acoustic Fingerprinting","✅","❌","⚡ Limited","❌","❌"),
        ("Album Art Auto-Download","✅","⚡ Manual","⚡ Limited","✅","❌"),
        ("Lyrics Auto-Download","✅","❌","❌","❌","❌"),
        ("Duplicate Detection","✅","⚡ Plugin","⚡ Limited","❌","❌"),
        ("Batch Processing 10k+ songs","✅","✅","✅","✅","⚡"),
        ("iTunes Integration","✅","✅","⚡","✅","✅"),
        ("Beginner-Friendly Interface","✅","❌","❌","✅","✅"),
        ("Windows Support","✅","✅","✅","✅","✅"),
        ("macOS Support","✅","✅","⚡","✅","✅"),
        ("Free Trial","✅","✅ Free","✅ Free","✅","✅"),
        ("Time for 10k songs","~30 min","Hours","Hours","Days","Days"),
    ]
    table_rows = "".join(f"<tr><td>{f}</td><td style='color:#16a34a;font-weight:700'>{c1}</td><td>{c2}</td><td>{c3}</td><td>{c4}</td><td>{c5}</td></tr>" for f,c1,c2,c3,c4,c5 in rows)
    return f"""<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>TidyMyMusic vs Mp3tag vs MusicBrainz Picard — Music Organizer Comparison 2025</title>
  <meta name="description" content="Compare TidyMyMusic vs Mp3tag, MusicBrainz Picard, MediaMonkey and manual editing. See why TidyMyMusic is the best music library organizer in 2025."/>
  <link rel="canonical" href="{SITE_DOMAIN}/compare.html"/>
  <style>:root{{--ha:#7c3aff;--hb:#5b21b6}} table{{width:100%;border-collapse:collapse;font-size:.88rem}} th,td{{padding:.85rem 1rem;border-bottom:1px solid var(--border);text-align:left}} th{{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;border-bottom:2px solid var(--border)}} tr:hover td{{background:#fafafa}} .hl{{color:#7c3aff;font-weight:700}}</style>
  {BASE_CSS}
</head><body>
{nav_html()}
<section class="hero"><div class="eyebrow">✦ Software Comparison 2025</div>
  <h1>TidyMyMusic vs<br><em>The Competition</em></h1>
  <p class="hsub">See how TidyMyMusic stacks up against Mp3tag, MusicBrainz Picard, MediaMonkey and manual editing.</p>
  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored">⬇ Download Free Trial</a>
</section>
<section style="background:#fff"><div class="container">
  <div class="sec-ey">Feature Comparison</div><h2>TidyMyMusic vs Top Alternatives</h2>
  <div style="overflow-x:auto;margin-top:2rem">
    <table>
      <thead><tr><th>Feature</th><th class="hl">TidyMyMusic ✦</th><th>Mp3tag</th><th>MusicBrainz Picard</th><th>MediaMonkey</th><th>Manual Editing</th></tr></thead>
      <tbody>{table_rows}</tbody>
    </table>
  </div>
  <div style="margin-top:2rem;color:var(--muted);font-size:.85rem">✅ = Full support &nbsp;⚡ = Partial/plugin required &nbsp;❌ = Not available</div>
</div></section>
<section><div class="container">
  <div class="sec-ey">Why TidyMyMusic Wins</div><h2>The Decisive Advantage</h2>
  <div class="grid2">
    <div class="card"><div class="fi">🔊</div><h3>Only Tool with Acoustic Fingerprinting</h3><p>While competitors require you to have some existing tag information to look up songs, TidyMyMusic identifies tracks purely by listening to the audio — works on completely blank files.</p></div>
    <div class="card"><div class="fi">⚡</div><h3>All-in-One vs Multiple Tools</h3><p>Mp3tag, MusicBrainz Picard, and duplicate removers are separate tools. TidyMyMusic replaces them all — tags, artwork, lyrics, duplicates in one app.</p></div>
    <div class="card"><div class="fi">👤</div><h3>No Technical Skills Required</h3><p>MusicBrainz Picard has a steep learning curve. Mp3tag requires manual configuration. TidyMyMusic works out of the box for any user level.</p></div>
    <div class="card"><div class="fi">🎵</div><h3>iTunes Native Integration</h3><p>Competitors often break iTunes libraries. TidyMyMusic is built for seamless iTunes integration — changes sync to iPhone automatically.</p></div>
  </div>
</div></section>
<div class="cta-strip"><h2>The Best Music Organizer, Proven</h2><p>Try TidyMyMusic free and see why millions choose it over every alternative.</p>
  <a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">🎶 Download TidyMyMusic Free</a>
</div>
{footer_html()}</body></html>"""


def page_blog():
    posts = [
        ("how-to-fix-unknown-artist-itunes", "How to Fix 'Unknown Artist' in iTunes (2025 Guide)", "Step-by-step guide to fixing all 'Unknown Artist', 'Unknown Album' and 'Track 01' entries in your iTunes library automatically.", "iTunes", "5 min read"),
        ("how-to-organize-10000-songs", "How to Organise 10,000 Songs Without Losing Your Mind", "Practical guide to cleaning up a large music collection using batch processing and acoustic fingerprinting technology.", "Organisation", "7 min read"),
        ("best-mp3-tagger-2025", "The Best MP3 Tagger Software in 2025 — Ranked & Reviewed", "We tested the top MP3 tagging tools and ranked them by accuracy, ease of use, and feature completeness.", "Reviews", "8 min read"),
        ("how-to-download-album-art", "How to Download Missing Album Art for Your Entire Library", "A complete guide to automatically finding and embedding album artwork for every song in your collection.", "Artwork", "4 min read"),
        ("remove-duplicate-songs-guide", "The Complete Guide to Removing Duplicate Songs", "How to find and safely remove duplicate tracks without accidentally deleting music you want to keep.", "Storage", "6 min read"),
        ("acoustic-fingerprinting-explained", "What is Acoustic Fingerprinting and How Does It Work?", "A plain-language explanation of how music recognition technology identifies songs from audio alone.", "Technology", "5 min read"),
        ("id3-tags-explained", "ID3 Tags Explained: What They Are and Why They Matter", "Everything you need to know about ID3 tags — the metadata system that powers your music library.", "Education", "6 min read"),
        ("flac-vs-mp3-organisation", "Organising FLAC vs MP3 Libraries — Key Differences", "How to handle tagging and organisation differently for lossless FLAC files compared to compressed MP3s.", "Formats", "5 min read"),
        ("music-library-before-iphone-sync", "5 Things to Fix in Your Music Library Before Syncing to iPhone", "Avoid sync errors and missing artwork by cleaning up your library first with these five essential steps.", "Devices", "4 min read"),
        ("itunes-duplicate-songs-fix", "How to Find and Delete Duplicate Songs in iTunes", "A complete walkthrough for finding and removing duplicate tracks from your iTunes library without losing data.", "iTunes", "5 min read"),
        ("music-organizer-for-audiophiles", "The Best Music Organizer Software for Audiophiles in 2025", "Audiophiles have specific needs — correct composer tags, conductor information, lossless support. Here's what works best.", "Audiophile", "7 min read"),
        ("vinyl-rip-tagging-guide", "How to Tag Your Vinyl Rips Correctly", "A step-by-step guide for properly tagging digitised vinyl recordings so they appear correctly in every music player.", "Vinyl", "6 min read"),
    ]
    cards = "".join(f"""
    <div class="card">
      <div style="font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ha);margin-bottom:.5rem">{cat} · {time}</div>
      <h3 style="margin-bottom:.5rem;font-size:1rem"><a href="{BASE_PATH}/blog/{slug}.html" style="color:var(--ink)">{title}</a></h3>
      <p style="font-size:.85rem">{excerpt}</p>
      <a href="{BASE_PATH}/blog/{slug}.html" style="font-size:.83rem;font-weight:600;color:var(--ha);display:inline-block;margin-top:.9rem">Read more →</a>
    </div>""" for slug,title,excerpt,cat,time in posts)
    return f"""<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>TidyMyMusic Blog — Music Library Organisation Tips &amp; Guides</title>
  <meta name="description" content="Music library organisation tips, guides and tutorials. Learn how to fix ID3 tags, download album art, remove duplicates, organise iTunes and more."/>
  <link rel="canonical" href="{SITE_DOMAIN}/blog.html"/>
  <style>:root{{--ha:#7c3aff;--hb:#5b21b6;--fa:rgba(124,58,255,.1)}}</style>
  {BASE_CSS}
</head><body>
{nav_html()}
<section class="hero"><div class="eyebrow">✦ Music Organisation Blog</div>
  <h1>Tips, Guides &amp;<br><em>Tutorials</em></h1>
  <p class="hsub">Everything you need to know about organising your music library — from beginner guides to deep dives.</p>
</section>
<section><div class="container">
  <div class="sec-ey">Latest Articles</div><h2>Music Library Organisation Guides</h2>
  <div class="grid2">{cards}</div>
</div></section>
<div class="cta-strip"><h2>Put the Guides Into Practice</h2><p>Download TidyMyMusic and follow along with any of our tutorials — free trial available.</p>
  <a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">🎶 Download TidyMyMusic Free</a>
</div>
{footer_html()}</body></html>"""


def page_keywords(keywords):
    cats = {}
    for k in keywords:
        cats.setdefault(k["cat"], []).append(k)
    sections = ""
    for cat, items in sorted(cats.items()):
        links = "".join('<a class="kw" href="' + BASE_PATH + '/{}.html">{}</a>'.format(k["slug"], k["keyword"]) for k in items)
        sections += f'<div style="margin-bottom:2.5rem"><h3 style="font-size:1rem;font-weight:700;text-transform:capitalize;margin-bottom:.75rem;color:var(--ha)">{cat.replace("-"," ").title()} ({len(items)})</h3><div class="kw-cloud">{links}</div></div>'
    return f"""<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>TidyMyMusic — All Music Organisation Topics ({len(keywords)}+ Keywords)</title>
  <meta name="description" content="Browse all {len(keywords)}+ music organisation topics covered by TidyMyMusic — from ID3 tags to album art, duplicates, formats, platforms, and more."/>
  <link rel="canonical" href="{SITE_DOMAIN}/keywords.html"/>
  <style>:root{{--ha:#7c3aff;--hb:#5b21b6;--fa:rgba(124,58,255,.1)}}</style>
  {BASE_CSS}
</head><body>
{nav_html()}
<section class="hero"><div class="eyebrow">✦ Complete Topic Directory</div>
  <h1>All Music Organisation<br><em>Topics &amp; Keywords</em></h1>
  <p class="hsub">{len(keywords)} targeted topics covering every aspect of music library management.</p>
</section>
<section><div class="container">
  <div class="sec-ey">Browse by Category</div>
  <h2>All Topics ({len(keywords)})</h2>
  {sections}
</div></section>
<div class="cta-strip"><h2>Ready to Organise Your Library?</h2><p>Download TidyMyMusic free — works on Windows and Mac.</p>
  <a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">🎶 Download TidyMyMusic Free</a>
</div>
{footer_html()}</body></html>"""


def page_download():
    return f"""<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Download TidyMyMusic Free — Music Library Organizer for Windows &amp; Mac</title>
  <meta name="description" content="Download TidyMyMusic free trial for Windows or Mac. The best music library organizer — fix ID3 tags, get album art, remove duplicates automatically."/>
  <link rel="canonical" href="{SITE_DOMAIN}/download.html"/>
  <style>:root{{--ha:#7c3aff;--hb:#5b21b6;--fa:rgba(124,58,255,.1)}}</style>
  {BASE_CSS}
  {schema_software()}
</head><body>
{nav_html()}
<section class="hero"><div class="eyebrow">✦ Free Trial Available</div>
  <h1>Download TidyMyMusic<br><em>Free Today</em></h1>
  <p class="hsub">Try TidyMyMusic on your own music library — no credit card required. Available for Windows and Mac.</p>
  <a href="{AFFILIATE_URL}" class="btn-p" target="_blank" rel="nofollow sponsored" style="font-size:1.15rem;padding:1rem 2.5rem">⬇ Download Free Trial</a>
  <p style="color:rgba(255,255,255,.5);font-size:.82rem;margin-top:1rem">Windows 7/8/10/11 · macOS 10.10+</p>
</section>
<section style="background:#fff"><div class="container">
  <div class="sec-ey">What You Get</div>
  <h2>Free Trial Includes</h2>
  <div class="grid2">
    <div class="card"><div class="fi">🏷️</div><h3>ID3 Tag Repair</h3><p>Fix missing and incorrect music tags automatically across your entire library.</p></div>
    <div class="card"><div class="fi">🖼️</div><h3>Album Artwork</h3><p>Download and embed high-resolution album art for every track.</p></div>
    <div class="card"><div class="fi">🗑️</div><h3>Duplicate Detection</h3><p>Find and remove duplicate songs to free up storage space.</p></div>
    <div class="card"><div class="fi">📝</div><h3>Lyrics Download</h3><p>Automatically fetch and embed song lyrics into your audio files.</p></div>
    <div class="card"><div class="fi">🔊</div><h3>Acoustic Fingerprinting</h3><p>Identify songs with no tags using advanced audio analysis technology.</p></div>
    <div class="card"><div class="fi">⚡</div><h3>Batch Processing</h3><p>Process thousands of songs in one click — complete your library in minutes.</p></div>
  </div>
</div></section>
<section><div class="container">
  <div class="sec-ey">System Requirements</div><h2>Compatible With Your Setup</h2>
  <div class="grid2">
    <div class="card"><h3>🖥️ Windows</h3><ul><li>Windows 7 / 8 / 10 / 11</li><li>32-bit and 64-bit</li><li>500MB free disk space</li><li>1GHz processor or faster</li><li>256MB RAM minimum</li></ul></div>
    <div class="card"><h3>🍎 macOS</h3><ul><li>macOS 10.10 Yosemite and above</li><li>Includes Sonoma &amp; Sequoia</li><li>500MB free disk space</li><li>Intel and Apple Silicon</li><li>256MB RAM minimum</li></ul></div>
  </div>
</div></section>
<div class="cta-strip">
  <h2>Download TidyMyMusic Now</h2>
  <p>Free trial · No credit card · Works on Windows &amp; Mac</p>
  <a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">⬇ Download Free Trial</a>
</div>
{footer_html()}</body></html>"""


# ─────────────────────────────────────────────
# 4. SITEMAP + ROBOTS
# ─────────────────────────────────────────────

def build_sitemap(keyword_slugs):
    essential = ["", "features", "how-it-works", "faq", "compare", "blog", "download", "keywords"]
    today = BUILD_DATE
    urls = ""
    for page in essential:
        path = f"/{page}.html" if page else "/"
        urls += f"  <url><loc>{SITE_DOMAIN}{path}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>{'1.0' if not page else '0.8'}</priority></url>\n"
    for slug in keyword_slugs:
        urls += f"  <url><loc>{SITE_DOMAIN}/{slug}.html</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>\n"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""


def build_robots():
    return f"""User-agent: *
Allow: /
Sitemap: {SITE_DOMAIN}/sitemap.xml
"""

# ─────────────────────────────────────────────
# 5. llms.txt
# ─────────────────────────────────────────────

def build_llms():
    return f"""# TidyMyMusic

> TidyMyMusic is a professional music library organizer by Wondershare that automatically fixes ID3 tags, fetches missing album artwork, downloads lyrics, removes duplicate songs, and tidies entire music collections in one click using acoustic fingerprinting technology.

## Key Capabilities
- Automatic ID3 tag repair (artist, album, title, year, genre, track number)
- Album artwork recovery and embedding
- Lyrics download and embedding
- Duplicate song detection and removal
- Batch processing for libraries of any size
- iTunes library integration (Mac & Windows)
- Local folder support (MP3, FLAC, M4A, WAV, WMA, OGG, AIFF)
- Acoustic fingerprinting — identifies songs with zero existing tags
- Manual tag override support

## Platforms
Windows 7/8/10/11 · macOS 10.10+

## Pricing
Free trial available. Full license via affiliate link.

## Purchase / Download
{AFFILIATE_URL}

## Developer
Wondershare Software Co., Ltd.

## Site Coverage
This site contains {len(KEYWORDS)}+ keyword-targeted pages covering every aspect of music library management including ID3 tagging, album art, lyrics, duplicate removal, platform-specific guides, and comparisons with competitor tools.

## Keywords Summary
Music library organizer, iTunes cleaner, ID3 tag fixer, album artwork downloader, duplicate song remover, music metadata editor, batch MP3 tagger, acoustic fingerprint music identification, music collection manager, fix mislabeled songs, missing album art fixer, MP3 tag editor software, music organizer Windows, music organizer Mac, lyrics downloader for MP3, TidyMyMusic, Wondershare TidyMyMusic
"""

# ─────────────────────────────────────────────
# 6. MAIN BUILD RUNNER
# ─────────────────────────────────────────────

def main():
    os.makedirs(DIST, exist_ok=True)
    os.makedirs(f"{DIST}/blog", exist_ok=True)

    print(f"Building TidyMyMusic SEO Site...")
    print(f"Total keywords: {len(KEYWORDS)}")

    # Essential pages
    pages = {
        "index.html": page_index(),
        "features.html": page_features(),
        "how-it-works.html": page_how_it_works(),
        "faq.html": page_faq(),
        "compare.html": page_compare(),
        "blog.html": page_blog(),
        "download.html": page_download(),
        "keywords.html": page_keywords(KEYWORDS),
    }
    for fname, html in pages.items():
        path = f"{DIST}/{fname}"
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✓ {fname}")

    # Keyword pages
    print(f"\nGenerating {len(KEYWORDS)} keyword pages...")
    for i, kw_data in enumerate(KEYWORDS):
        # Get related keywords (same category, nearby)
        same_cat = [k for k in KEYWORDS if k["cat"] == kw_data["cat"] and k["slug"] != kw_data["slug"]]
        diff_cat = [k for k in KEYWORDS if k["cat"] != kw_data["cat"]]
        related = (same_cat + diff_cat)[:18]

        html = build_keyword_page(kw_data, related)
        path = f"{DIST}/{kw_data['slug']}.html"
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        if (i+1) % 100 == 0:
            print(f"  ✓ {i+1}/{len(KEYWORDS)} keyword pages generated")

    print(f"  ✓ All {len(KEYWORDS)} keyword pages generated")

    # Sitemap
    sitemap = build_sitemap([k["slug"] for k in KEYWORDS])
    with open(f"{DIST}/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)
    print(f"\n  ✓ sitemap.xml ({len(KEYWORDS) + 8} URLs)")

    # Robots
    with open(f"{DIST}/robots.txt", "w", encoding="utf-8") as f:
        f.write(build_robots())
    print(f"  ✓ robots.txt")

    # llms.txt
    with open(f"{DIST}/llms.txt", "w", encoding="utf-8") as f:
        f.write(build_llms())
    print(f"  ✓ llms.txt")

    # GitHub Pages: _config.yml (disables Jekyll so .html files are served as-is)
    config_yml = """# GitHub Pages config for TidyMyMusic
# Disables Jekyll processing so all .html files are served directly
exclude: [build.py, build-report.json]
"""
    with open(f"{DIST}/_config.yml", "w", encoding="utf-8") as f:
        f.write(config_yml)
    print(f"  ✓ _config.yml (GitHub Pages)")

    # GitHub Pages: .nojekyll (prevents Jekyll from ignoring underscore files)
    with open(f"{DIST}/.nojekyll", "w") as f:
        f.write("")
    print(f"  ✓ .nojekyll")

    # 404 page for GitHub Pages
    html_404 = f"""<!DOCTYPE html>
<html lang="en"><head>
  <meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Page Not Found — TidyMyMusic</title>
  <meta http-equiv="refresh" content="3;url={SITE_DOMAIN}/" />
  <style>body{{font-family:system-ui,sans-serif;background:#1a1a2e;color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;margin:0}} h1{{font-size:3rem;margin-bottom:1rem}} p{{color:rgba(255,255,255,.6);margin-bottom:2rem}} a{{background:#7c3aff;color:#fff;padding:.75rem 2rem;border-radius:8px;text-decoration:none;font-weight:700}}</style>
</head><body>
  <div>
    <div style="font-size:4rem;margin-bottom:1rem">🎵</div>
    <h1>Page Not Found</h1>
    <p>Redirecting to the homepage in 3 seconds…</p>
    <a href="{SITE_DOMAIN}/">Go to TidyMyMusic Home</a>
  </div>
</body></html>"""
    with open(f"{DIST}/404.html", "w", encoding="utf-8") as f:
        f.write(html_404)
    print(f"  ✓ 404.html")

    # Build report
    total_files = len(pages) + len(KEYWORDS) + 6  # +6 for sitemap,robots,llms,_config,nojekyll,404
    total_size = sum(os.path.getsize(os.path.join(root, f))
                     for root, dirs, files in os.walk(DIST)
                     for f in files)

    report = {
        "build_date": BUILD_DATE,
        "total_pages": total_files,
        "keyword_pages": len(KEYWORDS),
        "essential_pages": list(pages.keys()),
        "categories": list(set(k["cat"] for k in KEYWORDS)),
        "total_size_kb": round(total_size / 1024, 1),
        "sitemap_urls": len(KEYWORDS) + 8,
        "affiliate_url": AFFILIATE_URL,
    }
    with open(f"{DIST}/build-report.json", "w") as f:
        json.dump(report, f, indent=2)
    print(f"  ✓ build-report.json")

    print(f"""
╔══════════════════════════════════════════════════╗
║          BUILD COMPLETE ✓                        ║
╠══════════════════════════════════════════════════╣
║  Keyword pages:     {len(KEYWORDS):>5}                        ║
║  Essential pages:   {len(pages):>5}                        ║
║  Total files:       {total_files:>5}                        ║
║  Sitemap URLs:      {len(KEYWORDS)+8:>5}                        ║
║  Total size:        {round(total_size/1024,1):>5} KB                      ║
║  Output:            ./dist/                      ║
╚══════════════════════════════════════════════════╝
""")

if __name__ == "__main__":
    main()
