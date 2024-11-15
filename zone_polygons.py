from shapely.geometry.polygon import Polygon

rift_zone_polygons = [
    # Blue Side Raptor Brush
    Polygon([(216 * 30, 148 * 30), (220 * 30, 164 * 30), (228 * 30, 166 * 30), (223 * 30, 148 * 30)]),

    # Blue Side Raptors (Inner)
    Polygon([(220 * 30, 164 * 30), (222 * 30, 191 * 30), (235 * 30, 198 * 30), (249 * 30, 193 * 30), (261 * 30, 179 * 30)]),

    # Blue Side Raptors (Outer)
    Polygon([(225 * 30, 150 * 30), (229 * 30, 167 * 30), (262 * 30, 179 * 30), (285 * 30, 160 * 30)]),

    # Blue Side Raptor Intersection
    Polygon([(285 * 30, 160 * 30), (261 * 30, 179 * 30), (272 * 30, 195 * 30), (309 * 30, 160 * 30)]),

    # Blue Side Raptor Ramp Entrance
    Polygon([(294 * 30, 173 * 30), (272 * 30, 195 * 30), (284 * 30, 205 * 30), (312 * 30, 185 * 30)]),

    # Behind Dragon Pit 1
    Polygon([(295 * 30, 131 * 30), (295 * 30, 160 * 30), (310 * 30, 160 * 30), (317 * 30, 127 * 30)]),

    # Behind Dragon Pit 2
    Polygon([(284 * 30, 105 * 30), (297 * 30, 131 * 30), (337 * 30, 122 * 30), (336 * 30, 96 * 30)]),

    # Blue Side Red Brush
    Polygon([(266 * 30, 117 * 30), (290 * 30, 133 * 30), (295 * 30, 131 * 30), (288 * 30, 117 * 30)]),

    # Blue Side Red Ramp Brush
    Polygon([(287 * 30, 133 * 30), (285 * 30, 160 * 30), (295 * 30, 160 * 30), (295 * 30, 132 * 30)]),

    # Blue Side Red Buff 1
    Polygon([(250 * 30, 108 * 30), (221 * 30, 120 * 30), (215 * 30, 147 * 30), (268 * 30, 157 * 30), (284 * 30, 130 * 30)]),

    # Blue Side Red Buff 2
    Polygon([(252 * 30, 107 * 30), (265 * 30, 117 * 30), (290 * 30, 117 * 30), (282 * 30, 105 * 30)]),

    # Blue Side Krugs Intersection Brush
    Polygon([(220 * 30, 101 * 30), (230 * 30, 116 * 30), (250 * 30, 108 * 30), (241 * 30, 93 * 30)]),

    # Blue Side Krugs Intersection 2
    Polygon([(229 * 30, 75 * 30), (250 * 30, 107 * 30), (258 * 30, 107 * 30), (265 * 30, 69 * 30)]),

    # Blue Side Krugs Intersection 1
    Polygon([(200 * 30, 60 * 30), (200 * 30, 79 * 30), (219 * 30, 100 * 30), (240 * 30, 93 * 30), (214 * 30, 60 * 30)]),

    # Blue Side Krugs
    Polygon([(266 * 30, 58 * 30), (258 * 30, 106 * 30), (305 * 30, 101 * 30), (315 * 30, 77 * 30), (279 * 30, 58 * 30)]),

    # Blue Side Krugs Brush
    Polygon([(296 * 30, 58 * 30), (295 * 30, 67 * 30), (315 * 30, 77 * 30), (331 * 30, 58 * 30)]),

    # Blue Side Red Shallow Cross
    Polygon([(261 * 30, 181 * 30), (234 * 30, 208 * 30), (247 * 30, 221 * 30), (274 * 30, 198 * 30)]),

    # Blue Side Red Gate Brush
    Polygon([(188 * 30, 104 * 30), (181 * 30, 115 * 30), (195 * 30, 122 * 30), (201 * 30, 110 * 30)]),

    # Blue Side Red Gate
    Polygon([(175 * 30, 60 * 30), (150 * 30, 133 * 30), (165 * 30, 145 * 30), (190 * 30, 100 * 30), (193 * 30, 60 * 30)]),

    # Blue Side Red Gate
    Polygon([(182 * 30, 117 * 30), (178 * 30, 123 * 30), (190 * 30, 132 * 30), (195 * 30, 123 * 30)]),

    # Blue Side Red Deep Path
    Polygon([(211 * 30, 92 * 30), (188 * 30, 142 * 30), (215 * 30, 147 * 30), (223 * 30, 105 * 30)]),

    # Blue Side Red Deep Cross
    Polygon([(187 * 30, 142 * 30), (187 * 30, 164 * 30), (205 * 30, 180 * 30), (221 * 30, 169 * 30), (215 * 30, 147 * 30)]),

    # Blue Side Red Dive Area
    Polygon([(341 * 30, 61 * 30), (316 * 30, 76 * 30), (307 * 30, 97 * 30), (365 * 30, 94 * 30), (382 * 30, 67 * 30), (367 * 30, 60 * 30)]),

    # Blue Side Red Tribrush
    Polygon([(336 * 30, 96 * 30), (337 * 30, 122 * 30), (368 * 30, 124 * 30), (372 * 30, 94 * 30)]),

    # Blue Side Wolves Ramp Brush
    Polygon([(170 * 30, 278 * 30), (158 * 30, 284 * 30), (174 * 30, 296 * 30), (184 * 30, 289 * 30)]),

    # Blue Side Wolves Ramp
    Polygon([(157 * 30, 284 * 30), (149 * 30, 287 * 30), (166 * 30, 300 * 30), (173 * 30, 296 * 30)]),
    
    # Blue Side Wolves Intersection 1
    Polygon([(149 * 30, 234 * 30), (129 * 30, 240 * 30), (130 * 30, 249 * 30), (152 * 30, 286 * 30), (180 * 30, 270 * 30)]),

    # Blue Side Wolves Intersection 2
    Polygon([(149 * 30, 222 * 30), (150 * 30, 233 * 30), (163 * 30, 246 * 30), (161 * 30, 218 * 30)]),

    # Blue Side Wolves Brush
    Polygon([(162 * 30, 218 * 30), (163 * 30, 246 * 30), (176 * 30, 245 * 30), (173 * 30, 215 * 30)]),

    # Blue Side Blue Deep Cross
    Polygon([(149 * 30, 194 * 30), (142 * 30, 222 * 30), (182 * 30, 212 * 30), (162 * 30, 192 * 30)]),

    # Blue Side Wolves
    Polygon([(114 * 30, 197 * 30), (99 * 30, 216 * 30), (101 * 30, 241 * 30), (138 * 30, 233 * 30), (149 * 30, 194 * 30)]),

    # Blue Side Blue Intersection 1
    Polygon([(79 * 30, 245 * 30), (59 * 30, 256 * 30), (59 * 30, 271 * 30), (131 * 30, 253 * 30), (128 * 30, 236 * 30)]),

    # Blue Side Blue Intersection 2
    Polygon([(79 * 30, 218 * 30), (79 * 30, 245 * 30), (100 * 30, 241 * 30), (99 * 30, 216 * 30)]),

    # Blue Side Blue Gate
    Polygon([(59 * 30, 176 * 30), (59 * 30, 191 * 30), (79 * 30, 218 * 30), (99 * 30, 216 * 30), (137 * 30, 169 * 30), (126 * 30, 154 * 30)]),

    # Blue Side Blue Buff
    Polygon([(98 * 30, 262 * 30), (110 * 30, 291 * 30), (127 * 30, 301 * 30), (147 * 30, 279 * 30), (131 * 30, 253 * 30)]),

    # Blue Side Gromp
    Polygon([(98 * 30, 262 * 30), (59 * 30, 272 * 30), (62 * 30, 303 * 30), (69 * 30, 313 * 30), (92 * 30, 308 * 30), (108 * 30, 290 * 30)]),

    # Blue Side Blue Tribrush
    Polygon([(59 * 30, 316 * 30), (59 * 30, 335 * 30), (71 * 30, 363 * 30), (91 * 30, 333 * 30), (88 * 30, 310 * 30)]),

    # Blue Side Blue Pocket
    Polygon([(94 * 30, 330 * 30), (78 * 30, 353 * 30), (89 * 30, 371 * 30), (111 * 30, 324 * 30)]),

    # Blue Side Blue Ramp Brush
    Polygon([(107 * 30, 289 * 30), (92 * 30, 307 * 30), (96 * 30, 324 * 30), (116 * 30, 296 * 30)]),

    # Blue Side Blue Ramp
    Polygon([(117 * 30, 295 * 30), (93 * 30, 329 * 30), (132 * 30, 317 * 30), (128 * 30, 302 * 30)]),

    # Blue Side Blue Shallow Cross
    Polygon([(197 * 30, 224 * 30), (170 * 30, 253 * 30), (200 * 30, 264 * 30), (220 * 30, 247 * 30)]),

    # Red Side Raptor Brush
    Polygon([(273 * 30, 334 * 30), (277 * 30, 352 * 30), (286 * 30, 353 * 30), (281 * 30, 336 * 30)]),

    # Red Side Raptors (Inner)
    Polygon([(266 * 30, 302 * 30), (252 * 30, 307 * 30), (240 * 30, 321 * 30), (280 * 30, 335 * 30), (279 * 30, 309 * 30)]),

    # Red Side Raptors (Outer)
    Polygon([(240 * 30, 322 * 30), (217 * 30, 341 * 30), (277 * 30, 352 * 30), (273 * 30, 334 * 30)]),

    # Red Side Raptor Intersection
    Polygon([(228 * 30, 306 * 30), (192 * 30, 341 * 30), (217 * 30, 341 * 30), (241 * 30, 318 * 30)]),

    # Red Side Raptor Ramp Entrance
    Polygon([(217 * 30, 293 * 30), (188 * 30, 316 * 30), (205 * 30, 327 * 30), (229 * 30, 305 * 30)]),

    # Behind Baron Pit 1
    Polygon([(191 * 30, 341 * 30), (184 * 30, 374 * 30), (206 * 30, 370 * 30), (206 * 30, 341 * 30)]),

    # Behind Baron Pit 2
    Polygon([(204 * 30, 370 * 30), (165 * 30, 379 * 30), (166 * 30, 405 * 30), (217 * 30, 396 * 30)]),

    # Red Side Red Brush
    Polygon([(207 * 30, 370 * 30), (213 * 30, 384 * 30), (236 * 30, 384 * 30), (211 * 30, 368 * 30)]),

    # Red Side Red Ramp Brush
    Polygon([(206 * 30, 341 * 30), (206 * 30, 369 * 30), (214 * 30, 368 * 30), (216 * 30, 341 * 30)]),

    # Red Side Red Buff 1
    Polygon([(233 * 30, 344 * 30), (217 * 30, 371 * 30), (251 * 30, 393 * 30), (280 * 30, 381 * 30), (286 * 30, 354 * 30)]),

    # Red Side Red Buff 2
    Polygon([(212 * 30, 384 * 30), (218 * 30, 396 * 30), (249 * 30, 394 * 30), (235 * 30, 384 * 30)]),

    # Red Side Krugs Intersection Brush
    Polygon([(249 * 30, 394 * 30), (259 * 30, 408 * 30), (280 * 30, 400 * 30), (271 * 30, 385 * 30)]),

    # Red Side Krugs Intersection 1
    Polygon([(243 * 30, 394 * 30), (236 * 30, 432 * 30), (272 * 30, 426 * 30), (250 * 30, 394 * 30)]),

    # Red Side Krugs Intersection 2
    Polygon([(282 * 30, 401 * 30), (260 * 30, 408 * 30), (286 * 30, 441 * 30), (301 * 30, 441 * 30)]),

    # Red Side Krugs
    Polygon([(196 * 30, 400 * 30), (186 * 30, 424 * 30), (223 * 30, 443 * 30), (235 * 30, 443 * 30), (243 * 30, 395 * 30)]),

    # Red Side Krugs Brush
    Polygon([(186 * 30, 424 * 30), (170 * 30, 443 * 30), (205 * 30, 443 * 30), (206 * 30, 443 * 30)]),

    # Red Side Red Shallow Cross
    Polygon([(254 * 30, 280 * 30), (228 * 30, 303 * 30), (240 * 30, 316 * 30), (268 * 30, 293 * 30)]),

    # Red Side Red Gate Brush
    Polygon([(306 * 30, 378 * 30), (300 * 30, 391 * 30), (313 * 30, 396 * 30), (319 * 30, 385 * 30)]),

    # Red Side Red Gate 1
    Polygon([(336 * 30, 357 * 30), (311 * 30, 401 * 30), (308 * 30, 441 * 30), (326 * 30, 441 * 30), (351 * 30, 368 * 30)]),

    # Red Side Red Gate 2
    Polygon([(311 * 30, 369 * 30), (306 * 30, 379 * 30), (319 * 30, 385 * 30), (323 * 30, 379 * 30)]),

    # Red Side Red Deep Path
    Polygon([(287 * 30, 354 * 30), (279 * 30, 395 * 30), (291 * 30, 410 * 30), (314 * 30, 359 * 30)]),

    # Red Side Red Deep Cross
    Polygon([(289 * 30, 312 * 30), (280 * 30, 332 * 30), (286 * 30, 354 * 30), (314 * 30, 359 * 30), (315 * 30, 336 * 30)]),

    # Red Side Red Dive Area
    Polygon([(135 * 30, 407 * 30), (120 * 30, 432 * 30), (137 * 30, 441 * 30), (155 * 30, 441 * 30), (184 * 30, 427 * 30), (194 * 30, 405 * 30)]),

    # Red Side Red Tribrush
    Polygon([(133 * 30, 375 * 30), (128 * 30, 407 * 30), (165 * 30, 405 * 30), (164 * 30, 379 * 30)]),

    # Red Side Wolves Ramp Brush
    Polygon([(327 * 30, 203 * 30), (315 * 30, 211 * 30), (332 * 30, 223 * 30), (344 * 30, 217 * 30)]),

    # Red Side Wolves Ramp
    Polygon([(326 * 30, 202 * 30), (344 * 30, 217 * 30), (353 * 30, 212 * 30), (333 * 30, 198 * 30)]),

    # Red Side Wolves Intersection 1
    Polygon([(348 * 30, 215 * 30), (313 * 30, 231 * 30), (351 * 30, 267 * 30), (371 * 30, 261 * 30), (370 * 30, 251 * 30)]),

    # Red Side Wolves Intersection 2
    Polygon([(338 * 30, 256 * 30), (340 * 30, 283 * 30), (352 * 30, 280 * 30), (351 * 30, 268 * 30)]),

    # Red Side Wolves Brush
    Polygon([(325 * 30, 257 * 30), (328 * 30, 286 * 30), (339 * 30, 284 * 30), (338 * 30, 255 * 30)]),

    # Red Side Blue Deep Cross
    Polygon([(318 * 30, 289 * 30), (339 * 30, 309 * 30), (352 * 30, 307 * 30), (358 * 30, 280 * 30)]),

    # Red Side Wolves
    Polygon([(361 * 30, 268 * 30), (351 * 30, 307 * 30), (386 * 30, 304 * 30), (401 * 30, 285 * 30), (399 * 30, 260 * 30)]),

    # Red Side Blue Intersection 1
    Polygon([(369 * 30, 248 * 30), (372 * 30, 265 * 30), (421 * 30, 256 * 30), (441 * 30, 245 * 30), (441 * 30, 230 * 30)]),

    # Red Side Blue Intersection 2
    Polygon([(401 * 30, 260 * 30), (402 * 30, 285 * 30), (422 * 30, 283 * 30), (422 * 30, 256 * 30)]),

    # Red Side Blue Gate
    Polygon([(401 * 30, 286 * 30), (364 * 30, 335 * 30), (375 * 30, 347 * 30), (442 * 30, 325 * 30), (442 * 30, 310 * 30), (422 * 30, 283 * 30)]),

    # Red Side Blue Buff
    Polygon([(373 * 30, 200 * 30), (353 * 30, 222 * 30), (369 * 30, 248 * 30), (401 * 30, 239 * 30), (390 * 30, 211 * 30)]),

    # Red Side Gromp
    Polygon([(392 * 30, 211 * 30), (402 * 30, 239 * 30), (441 * 30, 229 * 30), (438 * 30, 198 * 30), (431 * 30, 188 * 30), (408 * 30, 193 * 30)]),

    # Red Side Blue Tribrush
    Polygon([(429 * 30, 138 * 30), (409 * 30, 168 * 30), (412 * 30, 191 * 30), (441 * 30, 188 * 30), (441 * 30, 166 * 30)]),

    # Red Side Blue Pocket
    Polygon([(412 * 30, 131 * 30), (389 * 30, 175 * 30), (410 * 30, 168 * 30), (423 * 30, 149 * 30)]),

    # Red Side Blue Ramp Brush
    Polygon([(409 * 30, 170 * 30), (384 * 30, 205 * 30), (393 * 30, 211 * 30), (411 * 30, 189 * 30)]),

    # Red Side Blue Ramp
    Polygon([(408 * 30, 169 * 30), (369 * 30, 184 * 30), (373 * 30, 200 * 30), (384 * 30, 206 * 30)]),

    # Red Side Blue Shallow Cross
    Polygon([(311 * 30, 228 * 30), (281 * 30, 253 * 30), (305 * 30, 277 * 30), (331 * 30, 248 * 30)]),

    # Bot Line Brush
    Polygon([(266 * 30, 204 * 30), (254 * 30, 215 * 30), (288 * 30, 246 * 30), (302 * 30, 235 * 30)]),

    # Bot Mid River 1
    Polygon([(273 * 30, 197 * 30), (265 * 30, 205 * 30), (301 * 30, 235 * 30), (311 * 30, 228 * 30)]),

    # Bot Mid River 2
    Polygon([(304 * 30, 191 * 30), (285 * 30, 206 * 30), (302 * 30, 220 * 30), (320 * 30, 206 * 30)]),

    # Bot Pixel
    Polygon([(312 * 30, 185 * 30), (304 * 30, 191 * 30), (320 * 30, 206 * 30), (332 * 30, 198 * 30)]),

    # Dragon Pit
    Polygon([(317 * 30, 127 * 30), (309 * 30, 158 * 30), (334 * 30, 169 * 30), (360 * 30, 157 * 30), (362 * 30, 127 * 30)]),

    # Outside Dragon Pit (Higher)
    Polygon([(307 * 30, 181 * 30), (338 * 30, 202 * 30), (370 * 30, 188 * 30), (360 * 30, 158 * 30)]),

    # Outside Dragon Pit (Lower)
    Polygon([(376 * 30, 130 * 30), (361 * 30, 155 * 30), (369 * 30, 183 * 30), (389 * 30, 176 * 30), (403 * 30, 145 * 30)]),

    # Bot River Brush
    Polygon([(401 * 30, 108 * 30), (394 * 30, 140 * 30), (403 * 30, 146 * 30), (416 * 30, 122 * 30)]),

    # Bot Tribrush Entrance
    Polygon([(372 * 30, 107 * 30), (368 * 30, 124 * 30), (380 * 30, 130 * 30), (383 * 30, 103 * 30)]),

    # Bot River Mouth 1
    Polygon([(385 * 30, 93 * 30), (380 * 30, 131 * 30), (395 * 30, 138 * 30), (401 * 30, 108 * 30)]),

    # Bot River Mouth 2
    Polygon([(390 * 30, 97 * 30), (417 * 30, 122 * 30), (427 * 30, 110 * 30), (396 * 30, 83 * 30)]),

    # Top Line Brush
    Polygon([(212 * 30, 253 * 30), (200 * 30, 265 * 30), (235 * 30, 294 * 30), (247 * 30, 285 * 30)]),

    # Top Mid River 1
    Polygon([(200 * 30, 264 * 30), (191 * 30, 272 * 30), (227 * 30, 302 * 30), (235 * 30, 295 * 30)]),

    # Top Mid River 2
    Polygon([(199 * 30, 279 * 30), (181 * 30, 293 * 30), (197 * 30, 308 * 30), (216 * 30, 293 * 30)]),

    # Top Pixel
    Polygon([(181 * 30, 293 * 30), (168 * 30, 301 * 30), (187 * 30, 315 * 30), (197 * 30, 309 * 30)]),

    # Baron Pit
    Polygon([(168 * 30, 330 * 30), (141 * 30, 346 * 30), (139 * 30, 372 * 30), (184 * 30, 372 * 30), (192 * 30, 341 * 30)]),

    # Outside Baron Pit (Lower)
    Polygon([(162 * 30, 297 * 30), (131 * 30, 311 * 30), (141 * 30, 345 * 30), (190 * 30, 317 * 30)]),

    # Outside Baron Pit (Higher)
    Polygon([(132 * 30, 316 * 30), (112 * 30, 324 * 30), (98 * 30, 353 * 30), (127 * 30, 371 * 30), (140 * 30, 347 * 30)]),

    # Top River Brush
    Polygon([(98 * 30, 354 * 30), (85 * 30, 377 * 30), (100 * 30, 391 * 30), (107 * 30, 359 * 30)]),

    # Top Tribrush Entrance
    Polygon([(121 * 30, 369 * 30), (117 * 30, 396 * 30), (129 * 30, 392 * 30), (133 * 30, 375 * 30)]),

    # Top River Mouth 1
    Polygon([(106 * 30, 361 * 30), (100 * 30, 391 * 30), (116 * 30, 406 * 30), (121 * 30, 368 * 30)]),

    # Top River Mouth 2
    Polygon([(85 * 30, 378 * 30), (74 * 30, 397 * 30), (104 * 30, 421 * 30), (115 * 30, 409 * 30)]),

    # Mid Lane (Center)
    Polygon([(255 * 30, 215 * 30), (214 * 30, 254 * 30), (247 * 30, 284 * 30), (289 * 30, 245 * 30)]),

    # Blue Side Mid Outer Tower
    Polygon([(212 * 30, 187 * 30), (185 * 30, 212 * 30), (202 * 30, 227 * 30), (227 * 30, 203 * 30)]),

    # Blue Side Mid Outside Outer Tower
    Polygon([(227 * 30, 203 * 30), (203 * 30, 228 * 30), (221 * 30, 246 * 30), (247 * 30, 221 * 30)]),

    # Blue Side Mid Inner Tower
    Polygon([(166 * 30, 145 * 30), (137 * 30, 168 * 30), (160 * 30, 191 * 30), (186 * 30, 165 * 30)]),

    # Blue Side Mid Cross
    Polygon([(187 * 30, 166 * 30), (162 * 30, 191 * 30), (183 * 30, 211 * 30), (210 * 30, 186 * 30)]),

    # Red Side Mid Outer Tower
    Polygon([(300 * 30, 272 * 30), (274 * 30, 297 * 30), (288 * 30, 312 * 30), (318 * 30, 288 * 30)]),

    # Red Side Mid Outside Outer Tower
    Polygon([(282 * 30, 253 * 30), (254 * 30, 280 * 30), (272 * 30, 296 * 30), (300 * 30, 270 * 30)]),

    # Red Side Mid Inner Tower
    Polygon([(344 * 30, 315 * 30), (315 * 30, 337 * 30), (334 * 30, 355 * 30), (362 * 30, 334 * 30)]),

    # Red Side Mid Cross
    Polygon([(318 * 30, 288 * 30), (288 * 30, 312 * 30), (314 * 30, 337 * 30), (344 * 30, 314 * 30)]),

    # Bot Lane Brush Middle
    Polygon([(446 * 30, 52 * 30), (429 * 30, 66 * 30), (442 * 30, 78 * 30), (458 * 30, 63 * 30)]),

    # Bot Lane Brush Left
    Polygon([(441 * 30, 32 * 30), (406 * 30, 43 * 30), (421 * 30, 60 * 29), (438 * 30, 44 * 30)]),

    # Bot Lane Brush Right
    Polygon([(463 * 30, 74 * 30), (449 * 30, 86 * 30), (464 * 30, 101 * 30), (471 * 30, 99 * 30)]),

    # Bot Lane (Center) 1
    Polygon([(438 * 30, 44 * 30), (422 * 30, 58 * 30), (429 * 30, 64 * 30), (445 * 30, 51 * 30)]),

    # Bot Lane (Center) 2
    Polygon([(458 * 30, 64 * 30), (442 * 30, 78 * 30), (448 * 30, 85 * 30), (464 * 30, 71 * 30)]),

    # Bot Lane (Center) 3
    Polygon([(406 * 30, 44 * 30), (390 * 30, 78 * 30), (428 * 30, 110 * 30), (462 * 30, 101 * 30)]),

    # Bot Lane Alcove
    Polygon([(440 * 30, 6 * 30), (440 * 30, 42 * 30), (464 * 30, 72 * 30), (496 * 30, 63 * 30)]),

    # Blue Side Bot Lane Outer Tower
    Polygon([(344 * 30, 21 * 30), (343 * 30, 59 * 30), (369 * 30, 59 * 30), (374 * 30, 21 * 30)]),

    # Blue Side Bot Lane Outside Outer Tower
    Polygon([(374 * 30, 21 * 30), (369 * 30, 60 * 30), (392 * 30, 74 * 30), (414 * 30, 26 * 30)]),

    # Blue Side Bot Lane Inner Tower
    Polygon([(216 * 30, 21 * 30), (216 * 30, 59 * 30), (251 * 30, 58 * 30), (254 * 30, 21 * 30)]),

    # Blue Side Bot Lane Area
    Polygon([(254 * 30, 21 * 30), (252 * 30, 58 * 30), (341 * 30, 57 * 30), (343 * 30, 21 * 30)]),

    # Red Side Bot Lane Outer Tower
    Polygon([(480 * 30, 135 * 30), (440 * 30, 138 * 30), (442 * 30, 170 * 30), (480 * 30, 168 * 30)]),

    # Red Side Bot Lane Outside Outer Tower
    Polygon([(429 * 30, 111 * 30), (438 * 30, 137 * 30), (480 * 30, 135 * 30), (471 * 30, 100 * 30)]),

    # Red Side Bot Lane Inner Tower
    Polygon([(441 * 30, 259 * 30), (442 * 30, 296 * 30), (478 * 30, 295 * 30), (479 * 30, 257 * 30)]),

    # Red Side Bot Lane Area
    Polygon([(441 * 30, 171 * 30), (441 * 30, 258 * 30), (479 * 30, 257 * 30), (480 * 30, 168 * 30)]),

    # Top Lane Brush Middle
    Polygon([(59 * 30, 425 * 30), (42 * 30, 439 * 30), (54 * 30, 452 * 30), (71 * 30, 438 * 30)]),

    # Top Lane Brush Right
    Polygon([(78 * 30, 444 * 30), (62 * 30, 460 * 30), (89 * 30, 471 * 30), (94 * 30, 460 * 30)]),

    # Top Lane Brush Left
    Polygon([(36 * 30, 403 * 30), (29 * 30, 405 * 30), (36 * 30, 430 * 30), (51 * 30, 418 * 30)]),

    # Top Lane (Center) 1
    Polygon([(71 * 30, 438 * 30), (55 * 30, 453 * 30), (62 * 30, 459 * 30), (77 * 30, 445 * 30)]),

    # Top Lane (Center) 2
    Polygon([(52 * 30, 418 * 30), (36 * 30, 432 * 30), (42 * 30, 439 * 30), (57 * 30, 425 * 30)]),

    # Top Lane (Center) 3
    Polygon([(72 * 30, 394 * 30), (38 * 30, 403 * 30), (94 * 30, 460 * 30), (110 * 30, 426 * 30)]),

    # Top Lane Alcove
    Polygon([(35 * 30, 432 * 30), (10 * 30, 464 * 30), (66 * 30, 492 * 30), (60 * 30, 461 * 30)]),

    # Red Side Top Lane Outer Tower
    Polygon([(135 * 30, 442 * 30), (130 * 30, 475 * 30), (160 * 30, 475 * 30), (161 * 30, 442 * 30)]),

    # Red Side Top Lane Outside Outer Tower
    Polygon([(111 * 30, 428 * 30), (90 * 30, 472 * 30), (131 * 30, 475 * 30), (136 * 30, 441 * 30)]),

    # Red Side Top Lane Inner Tower
    Polygon([(253 * 30, 443 * 30), (250 * 30, 475 * 30), (288 * 30, 475 * 30), (288 * 30, 442 * 30)]),

    # Red Side Top Lane Area
    Polygon([(162 * 30, 444 * 30), (161 * 30, 475 * 30), (250 * 30, 475 * 30), (252 * 30, 443 * 30)]),

    # Blue Side Top Lane Outer Tower
    Polygon([(20 * 30, 340 * 30), (21 * 30, 373 * 30), (62 * 30, 371 * 30), (58 * 30, 338 * 30)]),

    # Blue Side Top Lane Outside Outer Tower
    Polygon([(21 * 30, 373 * 30), (29 * 30, 405 * 30), (71 * 30, 394 * 30), (62 * 30, 371 * 30)]),

    # Blue Side Top Lane Inner Tower
    Polygon([(22 * 30, 213 * 30), (21 * 30, 251 * 30), (59 * 30, 249 * 30), (58 * 30, 212 * 30)]),

    # Blue Side Top Lane Area
    Polygon([(21 * 30, 251 * 30), (20 * 30, 340 * 30), (59 * 30, 337 * 30), (59 * 30, 250 * 30)]),

    # Blue Side Base
    Polygon([(0 * 30, 0 * 30), (0 * 30, 170 * 30), (59 * 30, 176 * 30), (127 * 30, 154 * 30), (150 * 30, 132 * 30), (174 * 30, 61 * 30), (173 * 30, 0 * 30)]),

    # Blue Side Bot Inhib Entrance
    Polygon([(174 * 30, 21 * 30), (174 * 30, 60 * 30), (216 * 30, 59 * 30), (216 * 30, 21 * 30)]),

    # Blue Side Mid Inhib Entrance
    Polygon([(125 * 30, 155 * 30), (137 * 30, 168 * 30), (165 * 30, 144 * 30), (150 * 30, 133 * 30)]),

    # Blue Side Top Inhib Entrance
    Polygon([(23 * 30, 173 * 30), (22 * 30, 213 * 30), (58 * 30, 211 * 30), (58 * 30, 176 * 30)]),

    # Red Side Base
    Polygon([(500 * 30, 500 * 30), (328 * 30, 500 * 30), (327 * 30, 441 * 30), (351 * 30, 368 * 30), (375 * 30, 347 * 30), (443 * 30, 325 * 30), (500 * 30, 331 * 30)]),

    # Red Side Bot Inhib Entrance
    Polygon([(327 * 30, 441 * 30), (288 * 30, 442 * 30), (288 * 30, 475 * 30), (327 * 30, 475 * 30)]),

    # Red Side Mid Inhib Entrance
    Polygon([(363 * 30, 334 * 30), (334 * 30, 356 * 30), (350 * 30, 368 * 30), (375 * 30, 347 * 30)]),

    # Red Side Top Inhib Entrance
    Polygon([(442 * 30, 296 * 30), (443 * 30, 325 * 30), (478 * 30, 328 * 30), (478 * 30, 295 * 30)]),
]



