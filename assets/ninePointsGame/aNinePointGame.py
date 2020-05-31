"""Source code generating images in "a nine-point game" blog post."""

import numpy as np
import matplotlib.pyplot as plt


def angleToCenter(angle):
    return majorRadius * np.array([np.cos(angle), np.sin(angle)])


def centerToCircle(center):
    return plt.Circle(center, circleRadius, fc = circleColor, ec = 'black', zorder = zorderCircle)


def neighborCenterToLineSegment(center):
    x, y = center
    return plt.Line2D((0, x), (0, y), lw = lineWidth, color = lineColor, zorder = zorderLine)


def playerCenterToCircle(center, color):
    return plt.Circle(center, playerCircleRadius, fc = color, ec = color, zorder = zorderCircle)


def getEmptyBoard():
    fig = plt.figure(figsize = (3, 3))
    ax = fig.add_subplot()
    ax.set_aspect('equal')
    ax.axis('off')
    maxValue = majorRadius + circleRadius + 0.5
    ax.set_xlim(-maxValue, maxValue)
    ax.set_ylim(-maxValue, maxValue)

    centerCircle = plt.Circle(origin, circleRadius, fc = circleColor, ec = 'black', zorder = zorderCircle)
    neighborCircles = list(map(centerToCircle, neighborCenters))
    for circle in neighborCircles + [centerCircle]:
        ax.add_patch(circle)

    lineFromCenterToNeighbors = list(map(neighborCenterToLineSegment, neighborCenters))
    lineBetweenNeighborCircle = []
    for i in range(nNeighborCircles):
        x1, y1 = neighborCenters[i - 1]
        x2, y2 = neighborCenters[i]
        line = plt.Line2D((x1, x2), (y1, y2), lw = lineWidth, color = lineColor, zorder = zorderLine)
        lineBetweenNeighborCircle.append(line)
    for line in lineFromCenterToNeighbors + lineBetweenNeighborCircle:
        ax.add_line(line)
    return ax


def plotPlayersPositions(ax, firstPlayerIndex, secondPlayerIndex):
    firstPlayerCenters = [availablePositions[i] for i in firstPlayerIndex]
    firstPlayerCircles = list(map(playerCenterToCircle, firstPlayerCenters, ['tomato'] * len(firstPlayerIndex)))
    secondPlayerCenters = [availablePositions[i] for i in secondPlayerIndex]
    secondPlayerCircles = list(map(playerCenterToCircle, secondPlayerCenters, ['aqua'] * len(secondPlayerIndex)))
    for circle in firstPlayerCircles + secondPlayerCircles:
        ax.add_patch(circle)
    return None


# constants
majorRadius = 10
circleRadius = 1
playerCircleRadius = 0.7
origin = (0, 0)
circleColor = 'gray'
lineColor = 'black'
zorderCircle = 2
zorderLine = 1
nNeighborCircles = 8
lineWidth = 1
dpi = 300

angles = np.linspace(0, 2 * np.pi, endpoint = False, num = nNeighborCircles)
neighborCenters = list(map(angleToCenter, angles))
availablePositions = neighborCenters + [origin]
twoPlayersIndices = [
    [[1, 2, 3], [5, 6, 7]],
    [[1, 2, 3], [5, 6, 0]],
    [[1, 2, 4], [5, 6, 0]],
    [[1, 2, 4], [5, 8, 0]],
    [[1, 2, 3], [5, 8, 0]],
    [[1, 2, 3], [4, 8, 0]],
]

ax = getEmptyBoard()
plt.savefig('ninePointsGame_move_0.png', dpi = dpi)

for i, (firstPlayerIndex, secondPlayerIndex) in enumerate(twoPlayersIndices, start = 1):
    print(i)
    ax = getEmptyBoard()
    plotPlayersPositions(ax, firstPlayerIndex, secondPlayerIndex)
    plt.savefig(f'ninePointsGame_move_{i}.png', dpi = dpi)
    plt.close()
