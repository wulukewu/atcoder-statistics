<template>
  <div class="card">
    <div class="card-header">
      <div class="card-title">AtCoder Problems</div>
    </div>
    <div class="tabs">
      <div
        class="tab"
        :class="{ active: activeTab === 'table-abc' }"
        data-tab="table-abc"
        @click="showTab('table-abc')"
      >
        AtCoder Beginner Contest
      </div>
      <div
        class="tab"
        :class="{ active: activeTab === 'table-arc' }"
        data-tab="table-arc"
        @click="showTab('table-arc')"
      >
        AtCoder Regular Contest
      </div>
      <div
        class="tab"
        :class="{ active: activeTab === 'table-agc' }"
        data-tab="table-agc"
        @click="showTab('table-agc')"
      >
        AtCoder Grand Contest
      </div>
    </div>
    <div class="tables">
      <div
        v-for="tab in tabs"
        :key="tab.id"
        class="tab-content"
        :id="tab.id"
        :class="{ active: activeTab === tab.id }"
        ref="tabContents"
      >
        <div class="table-responsive">
          <table class="stats-table">
            <thead>
              <tr>
                <th>Score</th>
                <th>Grey</th>
                <th>Brown</th>
                <th>Green</th>
                <th>Cyan</th>
                <th>Blue</th>
                <th>Yellow</th>
                <th>Orange</th>
                <th>Red</th>
                <th>bronze</th>
                <th>silver</th>
                <th>gold</th>
              </tr>
            </thead>
            <tbody>
              <!-- Only show rows for ABC for now, but structure is ready for ARC/AGC -->
              <tr>
                <td class="score-label">100</td>
                <td>
                  <a href="lists/abc/100/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="100.0"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">345</span>
                      </div>
                      <span class="percentage color-grey">(100.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">150</td>
                <td>
                  <a href="lists/abc/150/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="100.0"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">21</span>
                      </div>
                      <span class="percentage color-grey">(100.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">200</td>
                <td>
                  <a href="lists/abc/200/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="95.17"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">315</span>
                      </div>
                      <span class="percentage color-grey">(95.17%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/200/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="4.23"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">14</span>
                      </div>
                      <span class="percentage color-brown">(4.23%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/200/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="0.6"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">2</span>
                      </div>
                      <span class="percentage color-green">(0.6%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">250</td>
                <td>
                  <a href="lists/abc/250/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="89.66"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">26</span>
                      </div>
                      <span class="percentage color-grey">(89.66%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/250/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="10.34"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">3</span>
                      </div>
                      <span class="percentage color-brown">(10.34%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">300</td>
                <td>
                  <a href="lists/abc/300/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="50.93"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">164</span>
                      </div>
                      <span class="percentage color-grey">(50.93%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/300/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="34.47"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">111</span>
                      </div>
                      <span class="percentage color-brown">(34.47%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/300/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="11.49"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">37</span>
                      </div>
                      <span class="percentage color-green">(11.49%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/300/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="3.11"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">10</span>
                      </div>
                      <span class="percentage color-cyan">(3.11%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">350</td>
                <td>
                  <a href="lists/abc/350/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="29.03"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">9</span>
                      </div>
                      <span class="percentage color-grey">(29.03%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/350/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="41.94"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">13</span>
                      </div>
                      <span class="percentage color-brown">(41.94%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/350/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="25.81"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">8</span>
                      </div>
                      <span class="percentage color-green">(25.81%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/350/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="3.23"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">1</span>
                      </div>
                      <span class="percentage color-cyan">(3.23%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">400</td>
                <td>
                  <a href="lists/abc/400/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="2.72"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">8</span>
                      </div>
                      <span class="percentage color-grey">(2.72%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/400/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="33.67"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">99</span>
                      </div>
                      <span class="percentage color-brown">(33.67%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/400/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="38.44"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">113</span>
                      </div>
                      <span class="percentage color-green">(38.44%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/400/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="19.05"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">56</span>
                      </div>
                      <span class="percentage color-cyan">(19.05%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/400/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="5.78"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">17</span>
                      </div>
                      <span class="percentage color-blue">(5.78%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/400/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="0.34"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">1</span>
                      </div>
                      <span class="percentage color-yellow">(0.34%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">425</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/425/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="25.0"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">8</span>
                      </div>
                      <span class="percentage color-brown">(25.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/425/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="62.5"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">20</span>
                      </div>
                      <span class="percentage color-green">(62.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/425/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="12.5"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">4</span>
                      </div>
                      <span class="percentage color-cyan">(12.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">450</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/450/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="2.27"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">1</span>
                      </div>
                      <span class="percentage color-brown">(2.27%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/450/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="27.27"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">12</span>
                      </div>
                      <span class="percentage color-green">(27.27%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/450/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="68.18"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">30</span>
                      </div>
                      <span class="percentage color-cyan">(68.18%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/450/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="2.27"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">1</span>
                      </div>
                      <span class="percentage color-blue">(2.27%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">475</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/475/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="32.56"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">14</span>
                      </div>
                      <span class="percentage color-green">(32.56%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/475/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="46.51"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">20</span>
                      </div>
                      <span class="percentage color-cyan">(46.51%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/475/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="18.6"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">8</span>
                      </div>
                      <span class="percentage color-blue">(18.6%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/475/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="2.33"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">1</span>
                      </div>
                      <span class="percentage color-yellow">(2.33%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">500</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/500/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="0.61"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">2</span>
                      </div>
                      <span class="percentage color-brown">(0.61%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/500/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="11.25"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">37</span>
                      </div>
                      <span class="percentage color-green">(11.25%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/500/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="38.3"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">126</span>
                      </div>
                      <span class="percentage color-cyan">(38.3%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/500/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="35.26"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">116</span>
                      </div>
                      <span class="percentage color-blue">(35.26%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/500/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="13.07"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">43</span>
                      </div>
                      <span class="percentage color-yellow">(13.07%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/500/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="1.52"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">5</span>
                      </div>
                      <span class="percentage color-orange">(1.52%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">525</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/525/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="2.7"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">1</span>
                      </div>
                      <span class="percentage color-green">(2.7%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/525/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="27.03"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">10</span>
                      </div>
                      <span class="percentage color-cyan">(27.03%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/525/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="51.35"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">19</span>
                      </div>
                      <span class="percentage color-blue">(51.35%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/525/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="18.92"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">7</span>
                      </div>
                      <span class="percentage color-yellow">(18.92%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">550</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/550/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="4.44"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">2</span>
                      </div>
                      <span class="percentage color-cyan">(4.44%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/550/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="46.67"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">21</span>
                      </div>
                      <span class="percentage color-blue">(46.67%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/550/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="40.0"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">18</span>
                      </div>
                      <span class="percentage color-yellow">(40.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/550/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="8.89"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">4</span>
                      </div>
                      <span class="percentage color-orange">(8.89%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">575</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/575/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="16.0"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">4</span>
                      </div>
                      <span class="percentage color-blue">(16.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/575/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="72.0"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">18</span>
                      </div>
                      <span class="percentage color-yellow">(72.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/575/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="4.0"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">1</span>
                      </div>
                      <span class="percentage color-orange">(4.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/575/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="4.0"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">1</span>
                      </div>
                      <span class="percentage color-red">(4.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/575/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="4.0"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">1</span>
                      </div>
                      <span class="percentage color-bronze">(4.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">600</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/600/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="0.32"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">1</span>
                      </div>
                      <span class="percentage color-green">(0.32%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/600/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="3.22"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">10</span>
                      </div>
                      <span class="percentage color-cyan">(3.22%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/600/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="10.93"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">34</span>
                      </div>
                      <span class="percentage color-blue">(10.93%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/600/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="31.19"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">97</span>
                      </div>
                      <span class="percentage color-yellow">(31.19%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/600/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="31.19"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">97</span>
                      </div>
                      <span class="percentage color-orange">(31.19%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/600/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="15.43"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">48</span>
                      </div>
                      <span class="percentage color-red">(15.43%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/600/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="6.75"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">21</span>
                      </div>
                      <span class="percentage color-bronze">(6.75%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/600/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="0.96"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">3</span>
                      </div>
                      <span class="percentage color-silver">(0.96%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">625</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/625/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="7.14"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">2</span>
                      </div>
                      <span class="percentage color-blue">(7.14%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/625/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="7.14"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">2</span>
                      </div>
                      <span class="percentage color-yellow">(7.14%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/625/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="35.71"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">10</span>
                      </div>
                      <span class="percentage color-orange">(35.71%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/625/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="42.86"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">12</span>
                      </div>
                      <span class="percentage color-red">(42.86%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/625/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="7.14"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">2</span>
                      </div>
                      <span class="percentage color-bronze">(7.14%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">650</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/650/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="5.26"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">1</span>
                      </div>
                      <span class="percentage color-yellow">(5.26%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/650/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="10.53"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">2</span>
                      </div>
                      <span class="percentage color-orange">(10.53%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/650/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="57.89"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">11</span>
                      </div>
                      <span class="percentage color-red">(57.89%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/650/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="26.32"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">5</span>
                      </div>
                      <span class="percentage color-bronze">(26.32%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">675</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/675/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="25.0"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">2</span>
                      </div>
                      <span class="percentage color-red">(25.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/675/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="37.5"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">3</span>
                      </div>
                      <span class="percentage color-bronze">(37.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/675/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="37.5"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">3</span>
                      </div>
                      <span class="percentage color-silver">(37.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">700</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/abc/700/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="50.0"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">2</span>
                      </div>
                      <span class="percentage color-blue">(50.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/700/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="25.0"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">1</span>
                      </div>
                      <span class="percentage color-yellow">(25.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/abc/700/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="25.0"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">1</span>
                      </div>
                      <span class="percentage color-orange">(25.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="tab-content" id="table-arc">
        <div class="table-responsive">
          <table class="stats-table">
            <thead>
              <tr>
                <th>Score</th>
                <th>Grey</th>
                <th>Brown</th>
                <th>Green</th>
                <th>Cyan</th>
                <th>Blue</th>
                <th>Yellow</th>
                <th>Orange</th>
                <th>Red</th>
                <th>bronze</th>
                <th>silver</th>
                <th>gold</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="score-label">100</td>
                <td>
                  <a href="lists/arc/100/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="100.0"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">1</span>
                      </div>
                      <span class="percentage color-grey">(100.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">200</td>
                <td>
                  <a href="lists/arc/200/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="66.67"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">2</span>
                      </div>
                      <span class="percentage color-grey">(66.67%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/200/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="33.33"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">1</span>
                      </div>
                      <span class="percentage color-brown">(33.33%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">300</td>
                <td>
                  <a href="lists/arc/300/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="56.14"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">32</span>
                      </div>
                      <span class="percentage color-grey">(56.14%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/300/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="31.58"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">18</span>
                      </div>
                      <span class="percentage color-brown">(31.58%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/300/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="12.28"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">7</span>
                      </div>
                      <span class="percentage color-green">(12.28%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">400</td>
                <td>
                  <a href="lists/arc/400/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="10.29"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">7</span>
                      </div>
                      <span class="percentage color-grey">(10.29%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/400/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="38.24"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">26</span>
                      </div>
                      <span class="percentage color-brown">(38.24%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/400/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="32.35"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">22</span>
                      </div>
                      <span class="percentage color-green">(32.35%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/400/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="17.65"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">12</span>
                      </div>
                      <span class="percentage color-cyan">(17.65%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/400/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="1.47"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">1</span>
                      </div>
                      <span class="percentage color-blue">(1.47%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">500</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/500/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="3.66"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">3</span>
                      </div>
                      <span class="percentage color-brown">(3.66%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/500/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="25.61"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">21</span>
                      </div>
                      <span class="percentage color-green">(25.61%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/500/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="45.12"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">37</span>
                      </div>
                      <span class="percentage color-cyan">(45.12%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/500/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="21.95"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">18</span>
                      </div>
                      <span class="percentage color-blue">(21.95%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/500/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="3.66"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">3</span>
                      </div>
                      <span class="percentage color-yellow">(3.66%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">600</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/600/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="3.16"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">3</span>
                      </div>
                      <span class="percentage color-green">(3.16%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/600/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="9.47"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">9</span>
                      </div>
                      <span class="percentage color-cyan">(9.47%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/600/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="41.05"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">39</span>
                      </div>
                      <span class="percentage color-blue">(41.05%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/600/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="38.95"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">37</span>
                      </div>
                      <span class="percentage color-yellow">(38.95%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/600/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="7.37"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">7</span>
                      </div>
                      <span class="percentage color-orange">(7.37%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">700</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/700/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="2.8"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">3</span>
                      </div>
                      <span class="percentage color-cyan">(2.8%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/700/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="4.67"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">5</span>
                      </div>
                      <span class="percentage color-blue">(4.67%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/700/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="37.38"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">40</span>
                      </div>
                      <span class="percentage color-yellow">(37.38%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/700/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="41.12"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">44</span>
                      </div>
                      <span class="percentage color-orange">(41.12%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/700/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="14.02"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">15</span>
                      </div>
                      <span class="percentage color-red">(14.02%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">800</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/800/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="12.5"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">10</span>
                      </div>
                      <span class="percentage color-yellow">(12.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/800/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="28.75"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">23</span>
                      </div>
                      <span class="percentage color-orange">(28.75%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/800/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="38.75"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">31</span>
                      </div>
                      <span class="percentage color-red">(38.75%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/800/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="17.5"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">14</span>
                      </div>
                      <span class="percentage color-bronze">(17.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/800/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="2.5"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">2</span>
                      </div>
                      <span class="percentage color-silver">(2.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">900</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/900/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="1.52"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">1</span>
                      </div>
                      <span class="percentage color-blue">(1.52%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/900/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="1.52"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">1</span>
                      </div>
                      <span class="percentage color-yellow">(1.52%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/900/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="19.7"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">13</span>
                      </div>
                      <span class="percentage color-orange">(19.7%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/900/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="34.85"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">23</span>
                      </div>
                      <span class="percentage color-red">(34.85%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/900/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="34.85"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">23</span>
                      </div>
                      <span class="percentage color-bronze">(34.85%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/900/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="7.58"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">5</span>
                      </div>
                      <span class="percentage color-silver">(7.58%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">1000</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/1000/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="2.13"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">1</span>
                      </div>
                      <span class="percentage color-yellow">(2.13%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1000/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="2.13"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">1</span>
                      </div>
                      <span class="percentage color-orange">(2.13%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1000/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="21.28"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">10</span>
                      </div>
                      <span class="percentage color-red">(21.28%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1000/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="36.17"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">17</span>
                      </div>
                      <span class="percentage color-bronze">(36.17%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1000/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="31.91"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">15</span>
                      </div>
                      <span class="percentage color-silver">(31.91%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1000/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="6.38"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">3</span>
                      </div>
                      <span class="percentage color-gold">(6.38%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">1100</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/1100/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="6.25"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">1</span>
                      </div>
                      <span class="percentage color-red">(6.25%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1100/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="43.75"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">7</span>
                      </div>
                      <span class="percentage color-bronze">(43.75%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1100/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="37.5"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">6</span>
                      </div>
                      <span class="percentage color-silver">(37.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1100/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="12.5"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">2</span>
                      </div>
                      <span class="percentage color-gold">(12.5%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">1200</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/1200/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="37.5"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">3</span>
                      </div>
                      <span class="percentage color-red">(37.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1200/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="37.5"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">3</span>
                      </div>
                      <span class="percentage color-bronze">(37.5%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1200/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="25.0"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">2</span>
                      </div>
                      <span class="percentage color-silver">(25.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">1300</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/1300/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="50.0"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">1</span>
                      </div>
                      <span class="percentage color-red">(50.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/arc/1300/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="50.0"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">1</span>
                      </div>
                      <span class="percentage color-bronze">(50.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">1500</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/1500/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="100.0"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">1</span>
                      </div>
                      <span class="percentage color-silver">(100.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">1600</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/arc/1600/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="100.0"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">1</span>
                      </div>
                      <span class="percentage color-silver">(100.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="tab-content" id="table-agc">
        <div class="table-responsive">
          <table class="stats-table">
            <thead>
              <tr>
                <th>Score</th>
                <th>Grey</th>
                <th>Brown</th>
                <th>Green</th>
                <th>Cyan</th>
                <th>Blue</th>
                <th>Yellow</th>
                <th>Orange</th>
                <th>Red</th>
                <th>bronze</th>
                <th>silver</th>
                <th>gold</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="score-label">200</td>
                <td>
                  <a href="lists/agc/200/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="42.86"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">6</span>
                      </div>
                      <span class="percentage color-grey">(42.86%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/200/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="35.71"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">5</span>
                      </div>
                      <span class="percentage color-brown">(35.71%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/200/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="21.43"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">3</span>
                      </div>
                      <span class="percentage color-green">(21.43%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">300</td>
                <td>
                  <a href="lists/agc/300/grey/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-grey"
                          data-color="var(--grey)"
                          data-percent="27.59"
                        >
                          <span class="progress-circle-inner bg-grey"></span>
                        </div>
                        <span class="count color-grey">8</span>
                      </div>
                      <span class="percentage color-grey">(27.59%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/300/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="37.93"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">11</span>
                      </div>
                      <span class="percentage color-brown">(37.93%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/300/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="27.59"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">8</span>
                      </div>
                      <span class="percentage color-green">(27.59%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/300/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="6.9"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">2</span>
                      </div>
                      <span class="percentage color-cyan">(6.9%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">400</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/400/brown/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-brown"
                          data-color="var(--brown)"
                          data-percent="16.0"
                        >
                          <span class="progress-circle-inner bg-brown"></span>
                        </div>
                        <span class="count color-brown">4</span>
                      </div>
                      <span class="percentage color-brown">(16.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/400/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="28.0"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">7</span>
                      </div>
                      <span class="percentage color-green">(28.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/400/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="20.0"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">5</span>
                      </div>
                      <span class="percentage color-cyan">(20.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/400/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="32.0"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">8</span>
                      </div>
                      <span class="percentage color-blue">(32.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/400/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="4.0"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">1</span>
                      </div>
                      <span class="percentage color-yellow">(4.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">500</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/500/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="57.14"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">8</span>
                      </div>
                      <span class="percentage color-cyan">(57.14%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/500/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="42.86"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">6</span>
                      </div>
                      <span class="percentage color-blue">(42.86%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">600</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/600/green/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-green"
                          data-color="var(--green)"
                          data-percent="10.53"
                        >
                          <span class="progress-circle-inner bg-green"></span>
                        </div>
                        <span class="count color-green">2</span>
                      </div>
                      <span class="percentage color-green">(10.53%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/600/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="21.05"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">4</span>
                      </div>
                      <span class="percentage color-cyan">(21.05%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/600/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="36.84"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">7</span>
                      </div>
                      <span class="percentage color-blue">(36.84%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/600/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="31.58"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">6</span>
                      </div>
                      <span class="percentage color-yellow">(31.58%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">700</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/700/cyan/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-cyan"
                          data-color="var(--cyan)"
                          data-percent="9.76"
                        >
                          <span class="progress-circle-inner bg-cyan"></span>
                        </div>
                        <span class="count color-cyan">4</span>
                      </div>
                      <span class="percentage color-cyan">(9.76%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/700/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="36.59"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">15</span>
                      </div>
                      <span class="percentage color-blue">(36.59%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/700/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="41.46"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">17</span>
                      </div>
                      <span class="percentage color-yellow">(41.46%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/700/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="12.2"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">5</span>
                      </div>
                      <span class="percentage color-orange">(12.2%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">800</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/800/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="17.65"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">6</span>
                      </div>
                      <span class="percentage color-blue">(17.65%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/800/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="38.24"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">13</span>
                      </div>
                      <span class="percentage color-yellow">(38.24%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/800/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="29.41"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">10</span>
                      </div>
                      <span class="percentage color-orange">(29.41%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/800/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="11.76"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">4</span>
                      </div>
                      <span class="percentage color-red">(11.76%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/800/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="2.94"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">1</span>
                      </div>
                      <span class="percentage color-bronze">(2.94%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">900</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/900/blue/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-blue"
                          data-color="var(--blue)"
                          data-percent="3.57"
                        >
                          <span class="progress-circle-inner bg-blue"></span>
                        </div>
                        <span class="count color-blue">1</span>
                      </div>
                      <span class="percentage color-blue">(3.57%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/900/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="17.86"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">5</span>
                      </div>
                      <span class="percentage color-yellow">(17.86%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/900/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="21.43"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">6</span>
                      </div>
                      <span class="percentage color-orange">(21.43%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/900/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="50.0"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">14</span>
                      </div>
                      <span class="percentage color-red">(50.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/900/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="7.14"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">2</span>
                      </div>
                      <span class="percentage color-bronze">(7.14%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">1000</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1000/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="29.03"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">9</span>
                      </div>
                      <span class="percentage color-orange">(29.03%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1000/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="38.71"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">12</span>
                      </div>
                      <span class="percentage color-red">(38.71%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1000/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="25.81"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">8</span>
                      </div>
                      <span class="percentage color-bronze">(25.81%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1000/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="6.45"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">2</span>
                      </div>
                      <span class="percentage color-silver">(6.45%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">1100</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1100/yellow/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-yellow"
                          data-color="var(--yellow)"
                          data-percent="8.7"
                        >
                          <span class="progress-circle-inner bg-yellow"></span>
                        </div>
                        <span class="count color-yellow">2</span>
                      </div>
                      <span class="percentage color-yellow">(8.7%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1100/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="26.09"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">6</span>
                      </div>
                      <span class="percentage color-orange">(26.09%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1100/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="34.78"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">8</span>
                      </div>
                      <span class="percentage color-red">(34.78%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1100/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="26.09"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">6</span>
                      </div>
                      <span class="percentage color-bronze">(26.09%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1100/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="4.35"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">1</span>
                      </div>
                      <span class="percentage color-silver">(4.35%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">1200</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1200/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="9.09"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">2</span>
                      </div>
                      <span class="percentage color-orange">(9.09%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1200/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="27.27"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">6</span>
                      </div>
                      <span class="percentage color-red">(27.27%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1200/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="36.36"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">8</span>
                      </div>
                      <span class="percentage color-bronze">(36.36%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1200/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="22.73"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">5</span>
                      </div>
                      <span class="percentage color-silver">(22.73%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1200/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="4.55"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">1</span>
                      </div>
                      <span class="percentage color-gold">(4.55%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">1300</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1300/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="18.18"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">2</span>
                      </div>
                      <span class="percentage color-orange">(18.18%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1300/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="18.18"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">2</span>
                      </div>
                      <span class="percentage color-red">(18.18%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1300/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="18.18"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">2</span>
                      </div>
                      <span class="percentage color-bronze">(18.18%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1300/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="27.27"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">3</span>
                      </div>
                      <span class="percentage color-silver">(27.27%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1300/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="18.18"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">2</span>
                      </div>
                      <span class="percentage color-gold">(18.18%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">1400</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1400/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="18.18"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">4</span>
                      </div>
                      <span class="percentage color-red">(18.18%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1400/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="31.82"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">7</span>
                      </div>
                      <span class="percentage color-bronze">(31.82%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1400/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="31.82"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">7</span>
                      </div>
                      <span class="percentage color-silver">(31.82%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1400/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="18.18"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">4</span>
                      </div>
                      <span class="percentage color-gold">(18.18%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">1500</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1500/orange/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-orange"
                          data-color="var(--orange)"
                          data-percent="7.14"
                        >
                          <span class="progress-circle-inner bg-orange"></span>
                        </div>
                        <span class="count color-orange">1</span>
                      </div>
                      <span class="percentage color-orange">(7.14%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1500/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="21.43"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">3</span>
                      </div>
                      <span class="percentage color-red">(21.43%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1500/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="28.57"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">4</span>
                      </div>
                      <span class="percentage color-bronze">(28.57%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1500/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="35.71"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">5</span>
                      </div>
                      <span class="percentage color-silver">(35.71%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1500/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="7.14"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">1</span>
                      </div>
                      <span class="percentage color-gold">(7.14%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">1600</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1600/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="13.04"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">3</span>
                      </div>
                      <span class="percentage color-red">(13.04%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1600/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="39.13"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">9</span>
                      </div>
                      <span class="percentage color-bronze">(39.13%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1600/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="43.48"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">10</span>
                      </div>
                      <span class="percentage color-silver">(43.48%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1600/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="4.35"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">1</span>
                      </div>
                      <span class="percentage color-gold">(4.35%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">1700</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1700/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="11.11"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">1</span>
                      </div>
                      <span class="percentage color-red">(11.11%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1700/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="33.33"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">3</span>
                      </div>
                      <span class="percentage color-bronze">(33.33%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1700/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="33.33"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">3</span>
                      </div>
                      <span class="percentage color-silver">(33.33%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1700/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="22.22"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">2</span>
                      </div>
                      <span class="percentage color-gold">(22.22%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">1800</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1800/red/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-red"
                          data-color="var(--red)"
                          data-percent="16.67"
                        >
                          <span class="progress-circle-inner bg-red"></span>
                        </div>
                        <span class="count color-red">2</span>
                      </div>
                      <span class="percentage color-red">(16.67%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1800/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="33.33"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">4</span>
                      </div>
                      <span class="percentage color-silver">(33.33%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1800/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="50.0"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">6</span>
                      </div>
                      <span class="percentage color-gold">(50.0%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">1900</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/1900/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="66.67"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">2</span>
                      </div>
                      <span class="percentage color-bronze">(66.67%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/1900/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="33.33"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">1</span>
                      </div>
                      <span class="percentage color-silver">(33.33%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">2000</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/2000/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="60.0"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">6</span>
                      </div>
                      <span class="percentage color-silver">(60.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/2000/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="40.0"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">4</span>
                      </div>
                      <span class="percentage color-gold">(40.0%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">2100</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/2100/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="100.0"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">1</span>
                      </div>
                      <span class="percentage color-gold">(100.0%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">2200</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/2200/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="50.0"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">2</span>
                      </div>
                      <span class="percentage color-bronze">(50.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/2200/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="25.0"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">1</span>
                      </div>
                      <span class="percentage color-silver">(25.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/2200/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="25.0"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">1</span>
                      </div>
                      <span class="percentage color-gold">(25.0%)</span>
                    </div></a
                  >
                </td>
              </tr>
              <tr>
                <td class="score-label">2300</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/2300/bronze/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-bronze"
                          data-color="var(--bronze)"
                          data-percent="100.0"
                        >
                          <span class="progress-circle-inner bg-bronze"></span>
                        </div>
                        <span class="count color-bronze">1</span>
                      </div>
                      <span class="percentage color-bronze">(100.0%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--silver)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--gold)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="score-label">2400</td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--grey)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--brown)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--green)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--cyan)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--blue)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--yellow)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--orange)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--red)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <div class="stats-container">
                    <div class="circle-container">
                      <div
                        class="progress-circle empty-color"
                        data-color="var(--bronze)"
                        data-percent="0.0"
                      >
                        <span class="progress-circle-inner"></span>
                      </div>
                      <span class="count empty-color">0</span>
                    </div>
                    <span class="percentage empty-color">(0.0%)</span>
                  </div>
                </td>
                <td>
                  <a href="lists/agc/2400/silver/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-silver"
                          data-color="var(--silver)"
                          data-percent="33.33"
                        >
                          <span class="progress-circle-inner bg-silver"></span>
                        </div>
                        <span class="count color-silver">1</span>
                      </div>
                      <span class="percentage color-silver">(33.33%)</span>
                    </div></a
                  >
                </td>
                <td>
                  <a href="lists/agc/2400/gold/" class="box-link"
                    ><div class="stats-container">
                      <div class="circle-container">
                        <div
                          class="progress-circle color-gold"
                          data-color="var(--gold)"
                          data-percent="66.67"
                        >
                          <span class="progress-circle-inner bg-gold"></span>
                        </div>
                        <span class="count color-gold">2</span>
                      </div>
                      <span class="percentage color-gold">(66.67%)</span>
                    </div></a
                  >
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick } from "vue";

export default {
  name: "AtcoderTable",
  setup() {
    // Tab state
    const tabs = [
      { id: "table-abc", label: "AtCoder Beginner Contest" },
      { id: "table-arc", label: "AtCoder Regular Contest" },
      { id: "table-agc", label: "AtCoder Grand Contest" },
    ];
    const activeTab = ref("table-abc");
    const tabContents = ref([]);

    // Animate progress circles
    function initializeProgressCircles() {
      const circles = document.querySelectorAll(
        ".tab-content.active .progress-circle"
      );
      circles.forEach((circle) => {
        const percent = parseFloat(circle.getAttribute("data-percent"));
        const innerCircle = circle.querySelector(".progress-circle-inner");
        setTimeout(() => {
          innerCircle.style.height = percent + "%";
        }, 500);
      });
    }

    // Set animation delay for table rows
    function setTableRowAnimations(tabId) {
      const rows = document.querySelectorAll(`#${tabId} .stats-table tbody tr`);
      rows.forEach((row, index) => {
        row.style.animationDelay = `${(index + 1) * 0.1}s`;
      });
    }

    // Tab switching
    function showTab(tabId) {
      activeTab.value = tabId;
      nextTick(() => {
        setTableRowAnimations(tabId);
        initializeProgressCircles();
      });
    }

    onMounted(() => {
      setTableRowAnimations(activeTab.value);
      initializeProgressCircles();
    });

    return {
      tabs,
      activeTab,
      showTab,
      tabContents,
    };
  },
};
</script>

<style scoped></style>
