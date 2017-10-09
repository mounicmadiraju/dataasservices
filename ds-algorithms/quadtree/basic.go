package main

import (
	"fmt"
	"github.com/mounicmadiraju/dataasservices/ds-algorithms/quadtree"
	"image"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().Unix())
	q := quadtree.QuadTree{
		MaxPointsPerNode: 2,
		BoundingBox:      image.Rect(0, 0, 500, 500),
	}

	for x := 0; x < 100; x++ {
		point := image.Point{rand.Intn(500), rand.Intn(500)}
		q.InsertPoint(point)
	}
	fmt.Println(q.Draw("qtree.png"))
}
