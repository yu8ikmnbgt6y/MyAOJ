#include<iostream>
#include<vector>
#include<queue>

static const int VERTEX_MAX = 100000;
using namespace std;


vector<int>     Graph[VERTEX_MAX];      //各頂点から他の頂点への出辺
int             Indegree[VERTEX_MAX];   //各頂点の入次数
bool            Used[VERTEX_MAX];       //各頂点のソート済みフラグ

int             num_vertex;
int             num_edge;
vector<int>     sorted_vertices;        //トポロジカルソートされた頂点


void breadth_first_search(int vertex) {
	queue<int> queue;
	queue.push(vertex);
	Used[vertex] = true;

	while (!queue.empty()) {
		int front_v = queue.front();
		queue.pop();

		//ここに来る頂点は入次数が0なのでソートされた行列にpushbackできる
		sorted_vertices.push_back(front_v);

		for (int i = 0; i < Graph[front_v].size(); i++) {
			int next_v = Graph[front_v][i];
			Indegree[next_v]--;								//front_vからの入辺がなくなるので入次数を一つ減らす

			if (Indegree[next_v] == 0 && !Used[next_v]) {	//入辺がなくなった頂点をキューに追加する
				Used[next_v] = true;
				queue.push(next_v);
			}
		}
	}
}



void topological_sort() {
	//入次数初期化
	for (int v_i = 0; v_i < num_vertex; v_i++) {
		Indegree[v_i] = 0;
	}
	//入力条件から入次数を入力
	for (int v_i = 0; v_i < num_vertex; v_i++) {
		for (int i = 0; i < Graph[v_i].size(); i++) {
			int v = Graph[v_i][i];
			Indegree[v]++;
		}
	}

	for (int v_i = 0; v_i < num_vertex; v_i++) {
		if (Indegree[v_i] == 0 && !Used[v_i]) {//源点か、現時点で入次数が0で未使用の頂点に対して幅優先探索
			breadth_first_search(v_i);
		}
	}
	return;
}


int main() {
	cin >> num_vertex >> num_edge;

	for (int i = 0; i < num_vertex; i++) {
		Used[i] = false;
	}

	int s, t;
	for (int i = 0; i < num_edge; i++) {
		cin >> s >> t;
		Graph[s].push_back(t);
	}

	topological_sort();

	for (vector<int>::iterator it = sorted_vertices.begin(); it != sorted_vertices.end(); ++it) {
		cout << *it << endl;
	}
	return 0;
}