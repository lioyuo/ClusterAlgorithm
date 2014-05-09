'''
implementation of graph
the following operations need to be implemented
1. Storage
2. add vertex
3. add edge
4. remove vertex
5. remove edge
6. query

A). Adjacency Matrix(V*V)
B). Adjacency List  (not sure about incident list or adjacency list) 
C). Incident Matrix(V*E)
'''

class AdjList(object):
	def __init__(self):
		self.vertices=[] #all nodes are different
		self.edges=[]
	
	def addVertex(self, node):
		if node in self.vertices:
			print 'node already in the graph'
		else:
			self.vertices.append(node)
	
	def addEdge(self, node1, node2, weight=1):
		edge=Edge(node1, node2, weight)
		self.edges.append(edge)

	def removeVertex(self, node):
		try:
			indexVertex=self.vertices.index(node)
		except Exception  as e:
			print 'node does not exist'
			return
		#remove any edge incident to the vertex
		removeIndex=[]
		for i in range(len(self.edges)):
			if self.edges[i].incident(node):
				removeIndex.append(i)
		for indexEdge in removeIndex:
			del self.edges[indexEdge]
		#remove the vertex
		del self.vertices[indexVertex]

	def removeEdge(self, edge):
		try:
			indexEdge=self.edges.index(edge)
		except Exception as e:
			print 'edge does not exist'
		del self.edges[index]

	def getVertexNumber(self):
		return len(self.vertices)

	def getEdgeNumber(self):
		return len(self.edges)

	def isConnected(self, node1, node2):
		if node1 == node2:
			return True
		for edge in self.edges:
			if (node1 in edge.nodes) and (node2 in edge.nodes):
				return True
			else:
				return False
	
	def toMatrix(self):
		'''
		the nodes information is lost, and they are replaced with the indices 1-n Vertex
		'''
		n = self.getVertexNumber()
		matrix = [[0 for i in range(n)] for j in range(n)]
		for edge in self.edges:
			node1, node2=edge.nodes
			index1=self.vertices.index(node1)
			index2=self.vertices.index(node2)
			matrix[index1][index2]=edge.weight
			matrix[index2][index1]=edge.weight

		return matrix
	
	def __repr__(self):
		matrix=self.toMatrix()
		nVertex=self.getVertexNumber()
		maxLen = max (max([len(str(element)) for element in matrix[i]]) for i in range(nVertex))
		result=''
		for i in range(nVertex):
			for j in range(nVertex):
				result+= '{0:>{1}} '.format(matrix[i][j], maxLen)
				#result += '%6g' %self.matrix[i][j] 
				#print '%4d' % self.matrix[i][j]
			result+='\n'
			#print '\n'
		return result
		#return repr(self.matrix)


class Vertex(object):
	def __init__(self, description):
		self.description=description
	
	def getDescription(self):
		return self.description

	def __repr__(self):
		return self.description


class Edge(object):
	def __init__(self, node1, node2, weight):
		self.nodes=[node1, node2]
		self.weight=weight
	
	def incident(node):
		if node in self.nodes:
			return True
		else:
			return False





class AdjMatrix(object):
	def __init__(self, n):
		'''
		initialize the graph of n vertices
		'''
		self.nVertex=n
		self.nEdge=0
		self.matrix=[[0 for i in range(self.nVertex)] for j in range(self.nVertex)]

	def addVertex(self):
		'''
		add a new vertex without any connection with the previous vertices.
		'''
		for l in range(self.nVertex):
			self.matrix[l].append(0)
		self.nVertex+=1
		self.matrix.append([0 for i in range(self.nVertex)])

	def addEdge(self, i, j, weight):
		if self.matrix[i][j] != 0:
			print 'the edge i-j already exist'
		else:
			self.matrix[i][j]=weight
			self.matrix[j][i]=weight
			self.nEdge+=1

	def removeEdge(self, i, j):
		if self.matrix[i][j] == 0:
			print 'the edge does not exist, no operation performed.'
		else:
			self.matrix[i][j]=0
			self.matrix[j][i]=0
		self.nEdge-=1

	def removeVertex(self, k):
		'''
		the vertices are renumbered, need to come up with better implementation
		'''
		for i in range(self.nVertex):
			del self.matrix[i][k]
		del self.matrix[k]
		self.nVertex-=1
		
	
	def getEdgeNumber(self):
		return self.nEdge

	def getVertexNumber(self):
		return self.nVertex

	def isConnected(self, i, j):
		if i >= self.nVertex or j >= self.nVertex:
			print 'error indices'
		else:
			return True if self.matrix[i][j] != 0 else False

	def __repr__(self):
		maxLen = max (max([len(str(element)) for element in self.matrix[i]]) for i in range(self.nVertex))
		result=''
		for i in range(self.nVertex):
			for j in range(self.nVertex):
				result+= '{0:>{1}} '.format(self.matrix[i][j], maxLen)
				#result += '%6g' %self.matrix[i][j] 
				#print '%4d' % self.matrix[i][j]
			result+='\n'
			#print '\n'
		return result
		#return repr(self.matrix)



def testAdjMatrix():
	'''
	testing Adjancency Matrix implementation
	'''
	n=4
	g=AdjMatrix(n)
	#g.addVertex()
	g.addEdge(0, 1, 1)
	g.addEdge(0, 2, 0.5)
	g.addEdge(2, 3, 2)
	g.addEdge(1, 2, 0.8)

	print g.getEdgeNumber()
	print g.getVertexNumber()
	print g.isConnected(0, 3)
	g.removeVertex(2)
	print g

def testAdjList():
	g=AdjList()
	n1=Vertex("node1")
	n2=Vertex("node2")
	n3=Vertex("node3")

	g.addVertex(n1)
	g.addVertex(n2)
	g.addVertex(n3)

	g.addEdge(n1, n2, 0.2)
	g.addEdge(n2, n3, 1)
	#g.addEdge(n1, n3, 2)

	print g.isConnected(n1, n2)
	print g.isConnected(n1, n3)
	
	print g


if __name__ == '__main__':
	testAdjMatrix()
	testAdjList()

