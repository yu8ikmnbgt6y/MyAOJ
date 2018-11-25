#include<iostream>
#include<vector>
#include<queue>

static const int VERTEX_MAX = 100000;
using namespace std;


vector<int>     Graph[VERTEX_MAX];      //�e���_���瑼�̒��_�ւ̏o��
int             Indegree[VERTEX_MAX];   //�e���_�̓�����
bool            Used[VERTEX_MAX];       //�e���_�̃\�[�g�ς݃t���O

int             num_vertex;
int             num_edge;
vector<int>     sorted_vertices;        //�g�|���W�J���\�[�g���ꂽ���_


void breadth_first_search(int vertex) {
	queue<int> queue;
	queue.push(vertex);
	Used[vertex] = true;

	while (!queue.empty()) {
		int front_v = queue.front();
		queue.pop();

		//�����ɗ��钸�_�͓�������0�Ȃ̂Ń\�[�g���ꂽ�s���pushback�ł���
		sorted_vertices.push_back(front_v);

		for (int i = 0; i < Graph[front_v].size(); i++) {
			int next_v = Graph[front_v][i];
			Indegree[next_v]--;								//front_v����̓��ӂ��Ȃ��Ȃ�̂œ�����������炷

			if (Indegree[next_v] == 0 && !Used[next_v]) {	//���ӂ��Ȃ��Ȃ������_���L���[�ɒǉ�����
				Used[next_v] = true;
				queue.push(next_v);
			}
		}
	}
}



void topological_sort() {
	//������������
	for (int v_i = 0; v_i < num_vertex; v_i++) {
		Indegree[v_i] = 0;
	}
	//���͏�����������������
	for (int v_i = 0; v_i < num_vertex; v_i++) {
		for (int i = 0; i < Graph[v_i].size(); i++) {
			int v = Graph[v_i][i];
			Indegree[v]++;
		}
	}

	for (int v_i = 0; v_i < num_vertex; v_i++) {
		if (Indegree[v_i] == 0 && !Used[v_i]) {//���_���A�����_�œ�������0�Ŗ��g�p�̒��_�ɑ΂��ĕ��D��T��
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